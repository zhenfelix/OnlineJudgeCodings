// class Solution {
// public:
//     bool dfs(vector<int> &piles, int i, int j, int a, int b, int flag){
//         if(i>j)return a>b;
//         if(flag==-1)return dfs(piles,i+1,j,a+piles[i],b,-flag) || dfs(piles,i,j-1,a+piles[j],b,-flag);
//         else return dfs(piles,i+1,j,a,b+piles[i],-flag) && dfs(piles,i,j-1,a,b+piles[j],-flag);
//     }
//     bool stoneGame(vector<int>& piles) {
//         return dfs(piles,0,piles.size()-1,0,0,-1);
//     }
// };
// time limit exceeded

// class Solution {
// public:

//     bool stoneGame(vector<int>& piles) {
//         int n=piles.size();
//         int sums=0;
//         vector<vector<int>> dp(n, vector<int>(n,0));
//         for(int i=0;i<n;i++){
//             dp[i][i]=piles[i];
//             sums+=piles[i];
//         }
//         for(int k=1;k<n;k++){
//             for(int j=k;j<n;j++){
//                 if(k%2==0){
//                     dp[j-k][j]=min(dp[j-k+1][j],dp[j-k][j-1]);
//                 }
//                 else{
//                     dp[j-k][j]=max(dp[j-k+1][j]+piles[j-k],dp[j-k][j-1]+piles[j]);
//                 }
                
//             }
//         }
//         return dp[0][n-1]>sums/2;
//     }
// };

//https://leetcode.com/problems/stone-game/discuss/154610/C++JavaPython-DP-or-Just-return-true
class Solution {
public:
        bool stoneGame(vector<int>& p) {
        int n = p.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) dp[i][i] = p[i];
        for (int d = 1; d < n; d++)
            for (int i = 0; i < n - d; i++)
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1]);
        return dp[0][n - 1] > 0;
    }
    
};