
class Solution {
public:
    int numDistinct(string s, string t) {
        int n = s.size(), m = t.size();
        vector<vector<unsigned>> dp(n+1,vector<unsigned>(m+1,0));
        for (int i = 0; i <= n; i++)
            dp[i][0] = 1;
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= i && j <= m; j++){
                dp[i][j] = dp[i-1][j];
                if (s[i-1] == t[j-1])
                    dp[i][j] += dp[i-1][j-1];
                // cout << i << " " << j << " " << dp[i][j] << endl;
            }
        }
        return dp[n][m];
    }
};



class Solution {
public:
    int numDistinct(string s, string t) {
        int n = s.size(), m = t.size();
        vector<unsigned>dp(m+1,0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++){
            for (int j = m; j > 0; j--){
                if (s[i-1] == t[j-1])
                    dp[j] += dp[j-1];
            }
        }
        return dp[m];
    }
};