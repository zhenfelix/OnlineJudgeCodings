int dp[111][111];
class Solution {
public:
    int getLengthOfOptimalCompression(string s, int k) {
        int n = s.size();
        memset(dp, 0x3f, sizeof(dp));
        dp[0][0] = 0;
        for(int i = 1; i <= n; i++) {
            for(int j = 0; j <= k; j++) {
                dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][j]);
                int cnt = 0, del = 0;
                for(int l = i; l <= n; l++) {
                    cnt += s[l - 1] == s[i - 1];
                    del += s[l - 1] != s[i - 1];
                    if(j + del <= k) dp[l][j + del] = min(dp[l][j + del], dp[i - 1][j] + 1 + (cnt >= 100 ? 3 : cnt >= 10 ? 2 : cnt >= 2 ? 1: 0));
                }
            }
        }
        return dp[n][k];
    }
};