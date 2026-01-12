#define MAXA ((int) 7e4)
bool inited = false;
vector<int> fac[MAXA + 5];
void init() {
    if (inited) return;
    inited = true;
    // 预处理每个数的因数
    for (int i = 1; i <= MAXA; i++) for (int j = i; j <= MAXA; j += i) fac[j].push_back(i);
}

class Solution {
public:
    int totalBeauty(vector<int>& nums) {
        init();
        int n = nums.size(), mx = 0;
        for (int x : nums) mx = max(mx, x);

        // 对于每个 gcd，把能被它整除的所有数挑出来
        vector<int> pos[mx + 1];
        for (int i = 0; i < n; i++) for (int x : fac[nums[i]]) pos[x].push_back(i);

        const int MOD = 1e9 + 7;
        // 求能被 K 整除的所有数形成的序列中，严格递增子序列有几个
        auto calc = [&](int K) {
            // 先离散化，方便用树状数组处理
            map<int, int> mp;
            for (int x : pos[K]) mp[nums[x]] = 1;
            int m = 0;
            for (auto &p : mp) p.second = ++m;
            vector<int> vec;
            for (int x : pos[K]) vec.push_back(mp[nums[x]]);

            // 树状数组模板开始

            long long tree[m + 1];
            memset(tree, 0, sizeof(tree));

            auto lb = [&](int x) { return x & (-x); };

            auto add = [&](int pos, long long val) {
                for (; pos <= m; pos += lb(pos)) tree[pos] = (tree[pos] + val) % MOD;
            };

            auto query = [&](int pos) {
                long long ret = 0;
                for (; pos; pos -= lb(pos)) ret = (ret + tree[pos]) % MOD;
                return ret;
            };

            // 树状数组模板结束

            long long ret = 0;
            for (int x : vec) {
                // 转移方程
                long long t = (query(x - 1) + 1) % MOD;
                add(x, t);
                ret = (ret + t) % MOD;
            }
            return ret;
        };

        long long f[mx + 1], ans = 0;
        // 先求 f(i) 表示 gcd 为 i 的倍数的严格递增子序列数量
        for (int i = 1; i <= mx; i++) f[i] = calc(i);
        // 再用容斥求出 gcd 恰为 i 的严格递增子序列数量
        for (int i = mx; i > 0; i--) {
            for (int j = i * 2; j <= mx; j += i) f[i] = (f[i] - f[j] + MOD) % MOD;
            ans = (ans + i * f[i]) % MOD;
        }
        return ans;
    }
};

// 作者：TsReaper
// 链接：https://leetcode.cn/problems/sum-of-beautiful-subsequences/solutions/3768184/rong-chi-shu-zhuang-shu-zu-by-tsreaper-f9hi/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。