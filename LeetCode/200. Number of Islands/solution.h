// class Solution {
    
// private:
//     vector<int> dx{0,0,-1,1},dy{-1,1,0,0};
// public:
//     void dfs(vector<vector<int>>& mat, int i, int j, int m, int n){
//         for(int k=0;k<4;k++){
//             if(i+dx[k]>=m||i+dx[k]<0||j+dy[k]>=n||j+dy[k]<0||(mat[i+dx[k]][j+dy[k]]!=1))continue;
//             mat[i+dx[k]][j+dy[k]]|=mat[i][j];
//             dfs(mat,i+dx[k],j+dy[k],m,n);
//         }
//         return;
//     }
//     int numIslands(vector<vector<char>>& grid) {
//         int cc=0,m=grid.size();
//         if(m==0)return 0;
//         int n=grid[0].size();
//         vector<vector<int>> mat(m,vector<int>(n,0));
//         for(int i=0;i<m;i++)for(int j=0;j<n;j++)mat[i][j]=grid[i][j]-'0';
        
//         for(int i=0;i<m;i++){
//             for(int j=0;j<n;j++){
//                 if(mat[i][j]==1){
//                     cc++;
//                     mat[i][j]|=(cc<<1);
//                     dfs(mat,i,j,m,n);
//                 }
//             }
//         }
//         return cc;
//     }
// };

class Solution {
private:
    int n;
    int m;
public:
    void visitNode(int row, int col, vector<vector<char>>& grid) {
        if (row < 0 || row >= n || col < 0 || col >= m || grid[row][col] == '0')
            return;
        grid[row][col] = '0';
        visitNode(row - 1, col, grid);
        visitNode(row + 1, col, grid);
        visitNode(row, col - 1, grid);
        visitNode(row, col + 1, grid);
    }
    
    int numIslands(vector<vector<char>>& grid) {
        n = grid.size();
        if (!n) return 0;
        m = grid[0].size();
        
        int islandCount = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    visitNode(i, j, grid);
                    islandCount++;
                }
            }
        }
        return islandCount;
    }
};