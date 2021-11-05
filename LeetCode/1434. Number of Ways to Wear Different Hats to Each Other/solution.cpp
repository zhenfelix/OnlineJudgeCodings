// using ll = long long;
// int MOD = 1e9+7;

// class Solution {
// public:
//     int numberWays(vector<vector<int>>& hats) {
//         int n = hats.size();
//         vector<vector<int>> h2p(41);
//         for (int i = 0; i < n; i++){
//             for (auto h : hats[i])
//                 h2p[h].push_back(i);
//         }
//         vector<int> dp(1<<n, 0);
//         dp[0] = 1;
//         for (int h = 1; h <= 40; h++){
//             vector<int> ndp = dp;
//             for (int s = 1; s < (1<<n); s++){
//                 for (auto i : h2p[h])
//                     if (s&(1<<i))
//                         ndp[s] = ((ll)ndp[s] + dp[s-(1<<i)])%MOD;
//             }
//             swap(dp,ndp);
//         }
//         return dp.back();
//     }
// };


using ll = long long;
const int MOD = 1e9+7;
const int maxn = 10;

int dp[1<<maxn];

class Solution {
public:
    int numberWays(vector<vector<int>>& hats) {
        int n = hats.size();
        vector<vector<int>> h2p(41);
        for (int i = 0; i < n; i++){
            for (auto h : hats[i])
                h2p[h].push_back(i);
        }
        memset(dp, 0, (1<<n)*sizeof(int));
        dp[0] = 1;
        for (int h = 1; h <= 40; h++){
            for (int s = (1<<n)-1; s ; s--){
                for (auto i : h2p[h])
                    if (s&(1<<i))
                        dp[s] = ((ll)dp[s] + dp[s-(1<<i)])%MOD;
            }
        }
        return dp[(1<<n)-1];
    }
};

