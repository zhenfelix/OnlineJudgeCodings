class Solution {
public:
    long long maxTaxiEarnings(int n, vector<vector<int>>& rides) {
        sort(rides.begin(), rides.end());
        vector<long long> dp(n + 1);
        int i = 0;
        for (auto &ride : rides) {
            while (i < ride[0]) {
                dp[i + 1] = max(dp[i + 1], dp[i]);
                i++;
            }
            dp[ride[1]] = max(dp[ride[1]], dp[ride[0]] + ride[1] - ride[0] + ride[2]);
        }
        while (i < n) {
            dp[i + 1] = max(dp[i + 1], dp[i]);
            i++;
        }
        return dp[n];
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/Uo2tRO/view/msfiPQ/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。