class Solution {
public:
    int maxSum(vector<int>& nums, int K, int m) {
        int n = nums.size();

        const long long INF = 1e18;
        // 常用常数优化：压缩第一维，防止超内存的同时，加快计算
        long long f[2][K + 1][m + 1];
        for (int j = 0; j <= K; j++) for (int k = 0; k <= m; k++) f[1][j][k] = -INF;
        f[1][1][0] = 0;

        auto update = [&](long long &a, long long b) { a = max(a, b); };

        long long ans = -INF;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= K; j++) for (int k = 0; k <= m; k++) f[i & 1][j][k] = -INF;
            for (int j = 1; j <= K; j++) {
                // 转移方程
                update(f[i & 1][j][0], f[i & 1 ^ 1][j][0]);
                update(f[i & 1][j][0], f[i & 1 ^ 1][j - 1][m]);
                update(f[i & 1][j][1], f[i & 1 ^ 1][j - 1][m] + nums[i]);
                update(f[i & 1][j][m], f[i & 1 ^ 1][j][m] + nums[i]);
                for (int k = 1; k <= m; k++) update(f[i & 1][j][k], f[i & 1 ^ 1][j][k - 1] + nums[i]);
            }
            update(ans, f[i & 1][K][m]);
        }
        return ans;
    }
};


// 作者：TsReaper
// 链接：https://leetcode.cn/circle/discuss/DmpDrr/view/Me75FL/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。