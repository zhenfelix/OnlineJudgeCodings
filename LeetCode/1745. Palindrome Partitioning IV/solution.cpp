const int maxn = 2005;
bitset<maxn> dp[maxn];

class Solution {
public:
    bool checkPartitioning(string s) {
        int n = s.length();
        for (int i = 0; i < n; i++)
            dp[i].set();
        for (int i = n-1; i >= 0; i--){
            for (int j = i+1; j < n; j++)
                if (dp[i+1][j-1] && s[i] == s[j])
                    dp[i][j] = 1;
                else
                    dp[i][j] = 0;
        }
        // for (int i = 0; i < n; i++)
        //     cout << dp[i] << endl;
        for (int i = 1; i < n; i++){
            for (int j = i; j < n-1; j++)
                if (dp[0][i-1] && dp[i][j] && dp[j+1][n-1])
                    return true;
        }
        // for (int i = 0; i < n; i++)
        //     cout << dp[i] << endl;
        return false;

    }
};