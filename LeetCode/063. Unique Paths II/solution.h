

// class Solution {
    
// public:
//     int helper(int m, int n, vector<vector<int>> &ans, vector<vector<int>>& obstacleGrid){
//         if(m<0||n<0)return 0;
//         if(obstacleGrid[obstacleGrid.size()-1-n][obstacleGrid[0].size()-1-m]==1)return 0;
//         if(ans[n][m]>0)return ans[n][m];
//         ans[n][m]=helper(m-1,n,ans,obstacleGrid)+helper(m,n-1,ans,obstacleGrid);
//         return ans[n][m];
//     }
//     int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
//         int n=obstacleGrid.size(),m=obstacleGrid[0].size();
//         vector<vector<int>> ans(n,vector<int>(m,0));
//         ans[0][0]=1;
//         return helper(m-1,n-1,ans,obstacleGrid);
//     }
// };

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m=obstacleGrid.size(),n=obstacleGrid[0].size();
        vector<vector<int>> np(m, vector<int>(n, 0));
        np[m-1][n-1] = 1;
        
        for (int i = m-1; i >= 0; --i) {
            for (int j = n-1; j >= 0; --j) {
                if(obstacleGrid[i][j]==1){
                    np[i][j]=0;continue;
                }
                if ((i+1) < m) {
                    np[i][j] += np[i+1][j];
                }
                if ((j+1) < n) {
                    np[i][j] += np[i][j+1];
                }
            }
        }
        
        return np[0][0];
    }
};