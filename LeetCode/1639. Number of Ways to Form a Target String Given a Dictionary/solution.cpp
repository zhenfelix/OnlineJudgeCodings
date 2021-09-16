using ll = long long;

class Solution {
public:
    int numWays(vector<string>& words, string target) {
        int sz = words.size(), m = words[0].length(), n = target.length();
        int MOD = 1e9+7;
        vector<vector<int>> cc(m,vector<int>(26,0));
        for (int i = 0; i < sz; i++){
            for (int j = 0; j < m; j++)
                cc[j][words[i][j]-'a']++;
        }
        vector<ll> dp(m,1);
        
        for (int i = 0; i < n; i++){
            ll pre = i == 0 ? 1 : 0;
            for (int j = 0; j < m; j++){
                int tmp = dp[j];
                dp[j] = j == 0 ? 0 : dp[j-1];
                dp[j] += pre*cc[j][target[i]-'a'];
                dp[j] %= MOD;
                pre = tmp;
            }
        }
        return dp.back();
    }
};