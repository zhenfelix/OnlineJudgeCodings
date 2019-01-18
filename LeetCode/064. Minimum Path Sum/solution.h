// class Solution {
// public:
//     int minPathSum(vector<vector<int>>& grid) {
//         int m=grid.size();
//         if(m==0)return 0;
//         int n=grid[0].size();
//         vector<int> ans(n,0);
//         for(int i=m-1;i>=0;i--){
//             for(int j=n-1;j>=0;j--){
//                 int a=INT_MAX,b=INT_MAX;
//                 if(i+1<=m-1)a=ans[j];
//                 if(j+1<=n-1)b=ans[j+1];
//                 ans[j]=grid[i][j]+min(a,b);
//                 if(i==m-1&&j==n-1)ans[j]=grid[i][j];
//             }
//         }
//         return ans[0];
//     }
// };

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m=grid.size();
        if(m==0)return 0;
        int n=grid[0].size();
        vector<int> ans(n,0);
        ans[n-1]=grid[m-1][n-1];
        for(int j=n-2;j>=0;j--)ans[j]=ans[j+1]+grid[m-1][j];
        for(int i=m-2;i>=0;i--){
            ans[n-1]+=grid[i][n-1];
            for(int j=n-2;j>=0;j--){
                ans[j]=grid[i][j]+min(ans[j],ans[j+1]);
            }
        }
        return ans[0];
    }
};