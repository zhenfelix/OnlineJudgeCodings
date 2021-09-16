// class Solution {
// public:
//     int m,n;
//     int memo[13][1<<12][2];
//     int connectTwoGroups(vector<vector<int>>& cost) {
//         m=cost.size();
//         n=cost[0].size();
//         memset(memo,-1,sizeof(memo));
//         return dfs(cost,0,0,0);
//     }
    
//     int dfs(vector<vector<int>>& cost, int idx ,int used, int part){
//         if(part==0 && idx==m){
//             if(memo[idx][used][part]!=-1) return memo[idx][used][part];
//             int res=dfs(cost,0,used,1);
//             return  memo[idx][used][part]= res;
//         }
//         if(part==1 && idx==n){
//             return 0;
//         }
        
//         if(memo[idx][used][part] !=-1) return memo[idx][used][part] ;
//         int res=INT_MAX;
//         if(part==0){
//             for(int i=0;i<n;i++){
            
//                 int next=dfs(cost,idx+1,used|(1<<i),part);
//                 if(next==INT_MAX) continue;
//                 res=min(res,cost[idx][i]+next);
            
//             }
//         }else{
//             if((used&(1<<idx)) !=0) res=dfs(cost,idx+1,used,1);
//             else {
//                 for(int i=0;i<m;i++){
//                     int next=dfs(cost,idx+1,used,1);
//                     if(next==INT_MAX) continue;
//                     res=min(res,cost[i][idx]+next);
//                 }
//             }
//         }
        
        
//         return memo[idx][used][part] = res;
        
//     }
// };



const int inf = 0x3f3f3f3f;

class Solution {
public:
    int connectTwoGroups(vector<vector<int>>& cost) {
        int n = cost.size(), m = cost[0].size(); 
        vector<int> micost(m);
        for (int j = 0; j < m; j++){
            micost[j] = inf;
            for (int i = 0; i < n; i++)
                micost[j] = min(micost[j], cost[i][j]);
        }
        vector<vector<int>> dp(n+1,vector<int>(1<<m,inf));

        function<int(int,int)> dfs = [&](int i, int mask){
            if (dp[i][mask] < inf)
                return dp[i][mask];
            if (i == n){
                int c = 0;
                for (int j = 0; j < m; j++){
                    if (((mask>>j)&1) == 0)
                        c += micost[j];
                }
                dp[i][mask] = c;
                return c;
            }
            for (int j = 0; j < m; j++){
                dp[i][mask] = min(dp[i][mask], cost[i][j]+dfs(i+1,mask|(1<<j)));
            }
            return dp[i][mask];
        };

        return dfs(0,0);
    }
};




const int inf = 0x3f3f3f3f;

class Solution {
public:
    int connectTwoGroups(vector<vector<int>>& cost) {
        int n = cost.size(), m = cost[0].size(); 
        vector<int> micost(m);
        for (int j = 0; j < m; j++){
            micost[j] = inf;
            for (int i = 0; i < n; i++)
                micost[j] = min(micost[j], cost[i][j]);
        }
        vector<vector<int>> dp(n+1,vector<int>(1<<m,inf));
        for (int mask = 0; mask < (1<<m); mask++){
            dp[n][mask] = 0;
            for (int j = 0; j < m; j++){
                if (((mask>>j)&1) == 0)
                    dp[n][mask] += micost[j];
            }
        }
        for (int i = n-1; i >= 0; i--){
            for (int mask = 0; mask < (1<<m); mask++){
                if (__builtin_popcount(mask) > i)
                    continue;
                for (int j = 0; j < m; j++){
                    dp[i][mask] = min(dp[i][mask], dp[i+1][mask|(1<<j)]+cost[i][j]);
                }
                if (i == 0)
                    break;
            }
        }
        return dp[0][0];

    }
};