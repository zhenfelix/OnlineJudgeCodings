class Solution {
public:
    int minSessions(vector<int>& tasks, int sessionTime) {
        int n = tasks.size();
        vector<int> sum(1 << n);
        for (int i = 1; i < (1 << n); ++i) {
            for (int j = 0; j < n; ++j) {
                if (i & (1 << j)) {
                    sum[i] = sum[i ^ (1 << j)] + tasks[j];
                    break;
                }
            }
        }
        
        vector<int> dp(1 << n, 1e9);
        dp[0] = 0;
        for (int i = 1; i < (1 << n); ++i) {
            for (int j = i; j; j = (j - 1) & i) {
                if (sum[j] > sessionTime)
                    continue;
                dp[i] = min(dp[i], dp[i ^ j] + 1);
            }
        }
        
        return dp[(1 << n) - 1];
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/be6FyL/view/MzzG67/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。