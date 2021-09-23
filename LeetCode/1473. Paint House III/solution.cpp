const int inf = 0x3f3f3f3f;

class Solution {
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
        vector<vector<vector<int>>> dp(target+1,vector<vector<int>>(m+1,vector<int>(n+1,inf)));
        dp[0][0][0] = 0;
        for (int t = 1; t <= target; t++){
            for (int len = 1; len <= m; len++){
                for (int c1 = 1; c1 <= n; c1++){
                    if (houses[len-1] != 0 && houses[len-1] != c1)
                        continue;
                    int ch = houses[len-1] == c1 ? 0 : cost[len-1][c1-1];
                    for (int c2 = 0; c2 <= n; c2++){
                        if (c1 == c2)
                            dp[t][len][c1] = min(dp[t][len][c1], dp[t][len-1][c2]+ch);
                        else
                            dp[t][len][c1] = min(dp[t][len][c1], dp[t-1][len-1][c2]+ch);
                    }
                }
            }
        }
        int res = *min_element(dp[target][m].begin(), dp[target][m].end());
        return res == inf ? -1 : res;
    }
};



const int inf = 0x3f3f3f3f;

class Solution {
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
        vector<vector<int>> dp(target+1,vector<int>(n+1,inf));
        dp[0][0] = 0;
        for (int len = 1; len <= m; len++){
            vector<vector<int>> ndp(target+1,vector<int>(n+1,inf));
            for (int t = 1; t <= target; t++){
                for (int c1 = 1; c1 <= n; c1++){
                    if (houses[len-1] != 0 && houses[len-1] != c1)
                        continue;
                    int ch = houses[len-1] == c1 ? 0 : cost[len-1][c1-1];
                    for (int c2 = 0; c2 <= n; c2++){
                        if (c1 == c2)
                            ndp[t][c1] = min(ndp[t][c1], dp[t][c2]+ch);
                        else
                            ndp[t][c1] = min(ndp[t][c1], dp[t-1][c2]+ch);
                    }
                }
            }
            swap(dp, ndp);
        }
        int res = *min_element(dp[target].begin(), dp[target].end());
        return res == inf ? -1 : res;
    }
};




const int maxt = 105, maxn = 25;
const int inf = 0x3f3f3f3f;

int dp[maxt][maxn], ndp[maxt][maxn];

class Solution {
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
        memset(dp, 0x3f, sizeof(int)*maxt*maxn);
        dp[0][0] = 0;
        for (int len = 1; len <= m; len++){
            memset(ndp, 0x3f, sizeof(int)*maxt*maxn);
            for (int t = 1; t <= target; t++){
                for (int c1 = 1; c1 <= n; c1++){
                    if (houses[len-1] != 0 && houses[len-1] != c1)
                        continue;
                    int ch = houses[len-1] == c1 ? 0 : cost[len-1][c1-1];
                    for (int c2 = 0; c2 <= n; c2++){
                        if (c1 == c2)
                            ndp[t][c1] = min(ndp[t][c1], dp[t][c2]+ch);
                        else
                            ndp[t][c1] = min(ndp[t][c1], dp[t-1][c2]+ch);
                    }
                }
            }
            swap(dp, ndp);
        }
        int res = inf;
        for (int c = 1; c <= n; c++)
            res = min(res, dp[target][c]);
        return res == inf ? -1 : res;
    }
};






const int maxt = 105, maxn = 25;
const int inf = 0x3f3f3f3f;

int dp[maxt][maxn], ndp[maxt][maxn];
int lo[maxt][maxn], nlo[maxt][maxn];
int hi[maxt][maxn], nhi[maxt][maxn];

class Solution {
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
        memset(dp, 0x3f, sizeof(int)*maxt*maxn);
        memset(lo, 0x3f, sizeof(int)*maxt*maxn);
        memset(hi, 0x3f, sizeof(int)*maxt*maxn);
        dp[0][0] = 0; hi[0][0] = 0;
        for (int c = 0; c <= n; c++)lo[0][c] = 0;
        for (int len = 1; len <= m; len++){
            memset(ndp, 0x3f, sizeof(int)*maxt*maxn);
            memset(nlo, 0x3f, sizeof(int)*maxt*maxn);
            memset(nhi, 0x3f, sizeof(int)*maxt*maxn);
            for (int t = 1; t <= target; t++){
                for (int c1 = 1; c1 <= n; c1++){
                    // if (houses[len-1] != 0 && houses[len-1] != c1)
                    //     continue;
                    // for (int c2 = 0; c2 <= n; c2++){
                    //     if (c1 == c2)
                    //         ndp[t][c1] = min(ndp[t][c1], dp[t][c2]);
                    //     else
                    //         ndp[t][c1] = min(ndp[t][c1], dp[t-1][c2]);
                    // }
                    if (houses[len-1] == 0 || houses[len-1] == c1){
                        int ch = houses[len-1] == c1 ? 0 : cost[len-1][c1-1];
                        ndp[t][c1] = min(dp[t][c1], lo[t-1][c1-1]);
                        if (c1 < n)
                            ndp[t][c1] = min(ndp[t][c1], hi[t-1][c1+1]);
                        ndp[t][c1] += ch;
                    }
                    nlo[t][c1] = min(ndp[t][c1], nlo[t][c1-1]);
                    nhi[t][c1] = ndp[t][c1];
                }
                for (int c = n; c > 0; c--)
                    nhi[t][c] = min(nhi[t][c], nhi[t][c+1]);
            }
            swap(dp, ndp);
            swap(lo, nlo);
            swap(hi, nhi);
        }
        int res = inf;
        for (int c = 1; c <= n; c++)
            res = min(res, dp[target][c]);
        return res == inf ? -1 : res;
    }
};







const int maxt = 105, maxn = 25;
const int inf = 0x3f3f3f3f;

int dp[maxt][maxn], ndp[maxt][maxn];


class Solution {
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
        memset(dp, 0x3f, sizeof(int)*maxt*maxn);
        dp[0][0] = 0;
        for (int len = 1; len <= m; len++){
            memset(ndp, 0x3f, sizeof(int)*maxt*maxn);
            for (int t = 1; t <= target; t++){
                int lo = dp[t-1][0];
                for (int c = 1; c <= n; c++){
                    if (houses[len-1] == 0 || houses[len-1] == c)
                        ndp[t][c] = min(dp[t][c], lo);
                    lo = min(lo, dp[t-1][c]);
                }
                int hi = inf;
                for (int c = n; c > 0; c--){
                    if (houses[len-1] == 0 || houses[len-1] == c)
                        ndp[t][c] = min(ndp[t][c], hi);
                    hi = min(hi, dp[t-1][c]);
                    int ch = houses[len-1] == c ? 0 : cost[len-1][c-1];
                    ndp[t][c] += ch;
                }
            }
            swap(dp, ndp);
        }
        int res = inf;
        for (int c = 1; c <= n; c++)
            res = min(res, dp[target][c]);
        return res == inf ? -1 : res;
    }
};