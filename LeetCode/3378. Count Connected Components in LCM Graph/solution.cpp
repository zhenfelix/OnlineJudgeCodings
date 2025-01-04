// 预处理每个数的因数
#define MAXA ((int) 2e5)
vector<int> fac[MAXA + 5];
bool inited = false;
void init() {
    if (inited) return;
    inited = true;
    for (int i = 1; i <= MAXA; i++) for (int j = i; j <= MAXA; j += i) fac[j].push_back(i);
}

class Solution {
public:
    int countComponents(vector<int>& nums, int threshold) {
        init();
        
        int n = nums.size();
        sort(nums.begin(), nums.end());
        // 记录小于等于 threshold 的每个数的因数
        vector<int> vec[threshold + 1];
        for (int i = 0; i < n; i++) if (nums[i] <= threshold)
            for (int f : fac[nums[i]]) vec[f].push_back(i);

        // 并查集模板
        int root[n];
        for (int i = 0; i < n; i++) root[i] = i;
        auto fr = [&](auto &&self, int x) -> int {
            if (root[x] != x) root[x] = self(self, root[x]);
            return root[x];
        };
        auto findroot = [&](int x) {
            return fr(fr, x);
        };

        // 枚举 gcd
        for (int g = 1; g <= threshold; g++) if (vec[g].size() > 0) {
            long long lim = 1LL * threshold * g;
            // 尝试让 gcd 的每个倍数都和最小的倍数连边
            for (int i = 1; i < vec[g].size(); i++)
                if (1LL * nums[vec[g][0]] * nums[vec[g][i]] <= lim) {
                    int x = findroot(vec[g][0]), y = findroot(vec[g][i]);
                    if (x != y) root[y] = x;
                }
        }

        // 统计连通块总数
        int ans = 0;
        for (int i = 0; i < n; i++) if (findroot(i) == i) ans++;
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/N44r7K/view/sN73gJ/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。