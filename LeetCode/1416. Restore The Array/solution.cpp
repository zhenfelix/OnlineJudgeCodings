using ll = long long;
const int MOD = 1e9+7;

class Solution {
public:
    int numberOfArrays(string s, int k) {
        int n = s.length();
        vector<int> dp(n+1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++){
            ll base = 1, cur = 0;
            for (int j = i; j >= i-9 && j >= 1; j--,base *= 10){
                if (s[j-1] == '0')
                    continue;
                cur += base*(s[j-1]-'0');
                if (cur > k)
                    break;
                // cout << i << " " << " " << j << " " << cur << endl;
                dp[i] = ((ll)dp[i] + dp[j-1])%MOD;
            }
        }
        return dp.back();
    }
};