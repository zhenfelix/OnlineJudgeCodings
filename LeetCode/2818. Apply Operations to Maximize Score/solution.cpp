#define MAXX ((int) 1e5)
int f[MAXX + 10];

bool inited = false;
// 预处理每个数有几个质因数
void init() {
    if (inited) return;
    inited = true;

    memset(f, 0, sizeof(f));
    for (int i = 2; i <= MAXX; i++) if (!f[i]) for (int j = i; j <= MAXX; j += i) f[j]++;
}

class Solution {
public:
    int maximumScore(vector<int>& nums, int K) {
        init();

        int n = nums.size();
        // 单调栈计算每个元素在哪个范围内是代表元素
        int L[n], R[n];
        for (int i = 0; i < n; i++) L[i] = -1, R[i] = n;
        stack<int> stk;
        for (int i = 0; i < n; i++) {
            while (!stk.empty() && f[nums[i]] > f[nums[stk.top()]]) R[stk.top()] = i, stk.pop();
            if (!stk.empty()) L[i] = stk.top();
            stk.push(i);
        }

        // 元素从大到小排序
        typedef pair<int, int> pii;
        vector<pii> vec;
        for (int i = 0; i < n; i++) vec.push_back(pii(-nums[i], i));
        sort(vec.begin(), vec.end());

        const int MOD = 1e9 + 7;
        // 快速幂求 a ** b
        auto power = [&](long long a, long long b) {
            long long y = 1;
            for (; b; b >>= 1) {
                if (b & 1) y = y * a % MOD;
                a = a * a % MOD;
            }
            return y;
        };

        long long ans = 1;
        // 从大到小考虑每个元素
        for (pii p : vec) {
            long long cnt = 1LL * (p.second - L[p.second]) * (R[p.second] - p.second);
            // 进行尽可能多次操作
            long long t = min(1LL * K, cnt);
            ans = ans * power(-p.first, t) % MOD, K -= t;
        }
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/9wQ08W/view/UkYzWR/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。