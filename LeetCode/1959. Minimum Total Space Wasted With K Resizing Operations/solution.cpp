const int INF = 0x3f3f3f3f;

class Solution {
public:
    int minSpaceWastedKResizing(vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, INF));
        dp[0][0] = 0;
        int hi = 0, sum = 0;
        for (int i = 0; i < n; ++i) {
            hi = max(hi, nums[i]);
            sum += nums[i];
            dp[i + 1][0] = hi * (i + 1) - sum;
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < k; ++j) {
                int hi = 0, sum = 0;
                for (int nxt = i + 1; nxt <= n; ++nxt) {
                    hi = max(hi, nums[nxt - 1]);
                    sum += nums[nxt - 1];
                    dp[nxt][j + 1] = min(dp[nxt][j + 1], dp[i][j] + hi * (nxt - i) - sum);
                }
            }
        }
        return dp[n][k];
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/9suuWs/view/8lA5Vo/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。