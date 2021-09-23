class Solution {
public:
    int longestAwesome(string s) {
        int n = s.length();
        vector<int> dp(1<<10,n);
        dp[0] = -1;
        int res = 1, cur = 0;
        for (int i = 0; i < n; i++){
            int j = s[i]-'0';
            cur ^= (1<<j);
            int pi = dp[cur];
            for (int k = 0; k < 10; k++)
                pi = min(pi, dp[cur^(1<<k)]);
            res = max(res, i-pi);
            dp[cur] = min(dp[cur],i);
        }
        return res;
    }
};