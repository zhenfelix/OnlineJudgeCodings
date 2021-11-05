using ll = long long;

const int MOD = 1e9+7;

class Solution {
public:
    int numOfArrays(int n, int m, int k) {
        vector<vector<int>> dp(m+1,vector<int>(k+1,0));
        dp[0][0] = 1;
        for (int len = 1; len <= n; len++){
            vector<vector<int>> ndp(m+1,vector<int>(k+1,0));
            for (int kk = 1; kk <= min(len,k); kk++){
                int lo = 0;
                
                for (int mm = 1; mm <= m; mm++){
                    lo = (lo+dp[mm-1][kk-1])%MOD;
                    ndp[mm][kk] = ((ll)dp[mm][kk]*mm+lo)%MOD;
                    // cout << len << " " << kk << " " << mm << " " << ndp[mm][kk] << endl;
                }
            }
            swap(dp,ndp);
        }
        int sums = 0;
        for (int mm = 1; mm <= m; mm++)
            sums = (sums+dp[mm][k])%MOD;
        return sums;
    }
};






// using ll = long long;

// const int MOD = 1e9+7;
// const int maxm = 105, maxk = 105;

// int dp[maxm][maxk], ndp[maxm][maxk];

// class Solution {
// public:
//     int numOfArrays(int n, int m, int k) {
//         memset(dp, 0, sizeof(int)*maxm*maxk);
//         dp[0][0] = 1;
//         for (int len = 1; len <= n; len++){
//             memset(ndp, 0, sizeof(int)*maxm*maxk);
//             for (int kk = 1; kk <= min(len,k); kk++){
//                 int lo = 0;
                
//                 for (int mm = 1; mm <= m; mm++){
//                     lo = (lo+dp[mm-1][kk-1])%MOD;
//                     ndp[mm][kk] = ((ll)dp[mm][kk]*mm+lo)%MOD;
//                     // cout << len << " " << kk << " " << mm << " " << ndp[mm][kk] << endl;
//                 }
//             }
//             swap(dp,ndp);
//         }
//         int sums = 0;
//         for (int mm = 1; mm <= m; mm++)
//             sums = (sums+dp[mm][k])%MOD;
//         return sums;
//     }
// };


using ll = long long;

const int MOD = 1e9+7;
const int maxm = 105, maxk = 105;

int dp[maxk][maxm], ndp[maxk][maxm];

class Solution {
public:
    int numOfArrays(int n, int m, int k) {
        memset(dp, 0, sizeof(int)*maxm*maxk);
        dp[0][0] = 1;
        for (int len = 1; len <= n; len++){
            memset(ndp, 0, sizeof(int)*maxm*maxk);
            for (int kk = 1; kk <= min(len,k); kk++){
                int lo = 0;
                
                for (int mm = 1; mm <= m; mm++){
                    lo = (lo+dp[kk-1][mm-1])%MOD;
                    ndp[kk][mm] = ((ll)dp[kk][mm]*mm+lo)%MOD;
                    // cout << len << " " << kk << " " << mm << " " << ndp[mm][kk] << endl;
                }
            }
            swap(dp,ndp);
        }
        int sums = 0;
        for (int mm = 1; mm <= m; mm++)
            sums = (sums+dp[k][mm])%MOD;
        return sums;
    }
};