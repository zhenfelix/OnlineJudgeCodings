class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int n = nums.size(), m = 0;
        for (int x : nums) m = max(m, x);

        const int INF = 1e9;
        // f[i][j]：前缀 max，即子序列最后一个元素值选择 i，倒数第二个元素值选择 <= j 的最大长度
        // g[i][j]：后缀 max，即子序列最后一个元素值选择 i，倒数第二个元素值选择 >= j 的最大长度
        // 注意到第二维的取值范围是 0 ~ m + 1，这是为了处理序列里只有一个元素的情况。我们认为 0 表示负无穷，m + 1 表示正无穷。
        int f[m + 2][m + 2], g[m + 2][m + 2];
        for (int i = 0; i <= m + 1; i++) for (int j = 0; j <= m + 1; j++) f[i][j] = g[i][j] = -INF;
        for (int j = 0; j <= m + 1; j++) f[nums[0]][j] = g[nums[0]][j] = 1;

        // 枚举子序列最后一个元素选什么
        for (int i = 1; i < n; i++) {
            int ff[m + 2], gg[m + 2];
            // 初始化：序列里只有一个元素的情况
            for (int j = 0; j <= m + 1; j++) ff[j] = gg[j] = 1;
            // 枚举倒数第二个元素选什么
            for (int j = 1; j <= m; j++) {
                int det = abs(nums[i] - j);
                int l = max(0, j - det), r = min(m + 1, j + det);
                ff[j] = gg[j] = max(f[j][l], g[j][r]) + 1;
            }
            // 前（后）缀 max
            for (int j = 1; j <= m + 1; j++) ff[j] = max(ff[j], ff[j - 1]);
            for (int j = m; j >= 0; j--) gg[j] = max(gg[j], gg[j + 1]);
            for (int j = 0; j <= m + 1; j++) {
                f[nums[i]][j] = max(f[nums[i]][j], ff[j]);
                g[nums[i]][j] = max(g[nums[i]][j], gg[j]);
            }
        }

        int ans = -INF;
        for (int i = 1; i <= m; i++) ans = max(ans, f[i][m + 1]);
        return ans;
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/longest-subsequence-with-decreasing-adjacent-difference/solutions/3038827/dp-qian-zhui-he-you-hua-by-tsreaper-qrq0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。