const int inf = 0x3f3f3f3f;

class Solution {
public:
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        int n = workers.size(), m = bikes.size();
        auto dist = [&](int i, int j){
            return abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1]);
        };
        vector<vector<int>> cost(n,vector<int>(m));
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++)
                cost[i][j] = dist(i,j);
        }
        vector<vector<int>> dp(n+1,vector<int>(1<<m,0));
        int res = inf;
        for (int i = 1; i <= n; i++){
            for (int s = 1; s < (1<<m); s++){
                if (__builtin_popcount(s) == i){
                    dp[i][s] = inf;
                    for (int j = 0; j < m; j++){
                        if ((s>>j)&1){
                            dp[i][s] = min(dp[i][s], dp[i-1][s-(1<<j)]+cost[i-1][j]);
                        }
                    }
                    if (i == n)
                        res = min(res, dp[i][s]);
                }
            }
        }
        return res;
    }
};