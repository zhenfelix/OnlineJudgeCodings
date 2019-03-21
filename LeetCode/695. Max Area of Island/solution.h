class Solution {
public:
    int dir[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
    int dfs(vector<vector<int>>& grid, int i, int j){
        if(i<0||j<0||i>=grid.size()||j>=grid[0].size()||grid[i][j]==0)return 0;
        int sums=1;
        grid[i][j]=0;
        for(int k=0;k<4;k++){
            sums+=dfs(grid,i+dir[k][0],j+dir[k][1]);
        }
        return sums;
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int area=0;
        // for(int i=0;i<grid.size();i++){
        //     dfs(grid,i,0);
        //     dfs(grid,i,grid[0].size()-1);
        // }
        // for(int j=0;j<grid[0].size();j++){
        //     dfs(grid,0,j);
        //     dfs(grid,grid.size()-1,j);
        // }
        for(int i=0;i<grid.size();i++){
            for(int j=0;j<grid[0].size();j++){
                area=max(area,dfs(grid,i,j));
            }
        }
        return area;
    }
};