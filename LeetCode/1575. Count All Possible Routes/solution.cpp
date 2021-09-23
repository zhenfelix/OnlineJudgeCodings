using ll = long long;

const int maxn = 105;
const int maxf = 205;
const int inf = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
ll dp[maxf][maxn], sumsl[maxf][maxn], sumsr[maxf][maxn];

class Solution
{
public:
    int countRoutes(vector<int> &locations, int start, int finish, int fuel)
    {
        memset(dp, 0, maxf * maxn * sizeof(ll));
        memset(sumsl, 0, maxf * maxn * sizeof(ll));
        memset(sumsr, 0, maxf * maxn * sizeof(ll));
        int n = locations.size();
        int sv = locations[start];
        int fv = locations[finish];
        sort(locations.begin(), locations.end());
        for (int i = 0; i < n; i++){
            if (locations[i] == sv)
                start = i;
            if (locations[i] == fv)
                finish = i;
        }
            
        dp[fuel][start] = 1;
        for (int f = fuel; f >= 0; f--)
        {
            for (int i = 0; i < n; i++)
            {
                if (f < fuel)
                    dp[f][i] = (sumsl[f][i]+sumsr[f][i])%MOD;
                int ff;
                if (i > 0 && ((ff = f - abs(locations[i - 1] - locations[i])) >= 0))
                    sumsr[ff][i - 1] = (sumsr[f][i] + dp[f][i]) % MOD;
                if (i < n - 1 && ((ff = f - abs(locations[i] - locations[i + 1])) >= 0))
                    sumsl[ff][i + 1] = (sumsl[f][i] + dp[f][i]) % MOD;
            }
        }
        ll res = 0;
        for (int f = 0; f <= fuel; f++)
        {
            res += dp[f][finish];
            res %= MOD;
        }
        return res;
    }
};





using ll = long long;

const int maxn = 105;
const int maxf = 205;
const int inf = 0x3f3f3f3f;
const int MOD = 1e9+7;
ll dp[maxf][maxn];

class Solution {
public:
    int countRoutes(vector<int>& locations, int start, int finish, int fuel) {
        memset(dp,0,maxf*maxn*sizeof(ll));
        int n = locations.size();
        // cout << n << endl;
        dp[fuel][start] = 1;
        for (int f = fuel; f > 0; f--){
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    int cost = abs(locations[i]-locations[j]);
                    if (j != i && cost <= f){
                        dp[f-cost][j] += dp[f][i];
                        dp[f-cost][j] %= MOD;
                    }
                }
            }
        }
        ll res = 0;
        for (int f = 0; f <= fuel; f++){
            res += dp[f][finish];
            res %= MOD;
        }
        return res;
    }
};



// using ll = long long;

// const int maxn = 105;
// const int maxf = 205;
// const int inf = 0x3f3f3f3f;
// const int MOD = 1e9+7;
// ll dp[maxf][maxn];

// class Solution {
// public:
//     int countRoutes(vector<int>& locations, int start, int finish, int fuel) {
//         memset(dp,0,maxf*maxn*sizeof(ll));
//         int n = locations.size();
//         // cout << n << endl;
//         dp[fuel][start] = 1;
//         for (int f = fuel-1; f >= 0; f--){
//             for (int i = 0; i < n; i++){
//                 dp[f][i] += dp[f+1][i];
//                 dp[f][i] %= MOD;
//                 for (int j = 0; j < n; j++){
//                     int cost = abs(locations[i]-locations[j]);
//                     if (i != j && f+cost <= fuel){
//                         dp[f][i] += dp[f+cost][j];
//                         dp[f][i] %= MOD;
//                         if (f+cost+1 <= fuel){
//                             dp[f][i] += MOD;
//                             dp[f][i] -= dp[f+cost+1][j];
//                             dp[f][i] %= MOD;
//                         }
//                     }
//                 }
//             }
//         }
//         // ll res = 0;
//         // for (int f = 0; f <= fuel; f++){
//         //     res += dp[f][finish];
//         //     res %= MOD;
//         // }
//         return dp[0][finish];
//     }
// };
