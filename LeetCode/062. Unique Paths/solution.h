// class Solution {
    
// public:
//     int helper(int m, int n, vector<vector<int>> &ans){
//         if(m<0||n<0)return 0;
//         if(ans[n][m]>0)return ans[n][m];
//         ans[n][m]=helper(m-1,n,ans)+helper(m,n-1,ans);
//         return ans[n][m];
//     }
//     int uniquePaths(int m, int n) {
//         vector<vector<int>> ans(n,vector<int>(m,0));
//         ans[0][0]=1;
//         return helper(m-1,n-1,ans);
//     }
// };

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> np(m, vector<int>(n, 0));
        np[m-1][n-1] = 1;
        
        for (int i = m-1; i >= 0; --i) {
            for (int j = n-1; j >= 0; --j) {
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