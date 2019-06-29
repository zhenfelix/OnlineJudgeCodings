class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int n = grid.size();
        if(n==0)return 0;
        int m = grid[0].size();
        int pre=0;
        int ans=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]!=pre){
                    pre=grid[i][j];
                    ans++;
                }
            }
            if(pre==1){
                pre=0;
                ans++;
            }
        }
        
        for(int j=0;j<m;j++){
            for(int i=0;i<n;i++){
                if(grid[i][j]!=pre){
                    pre=grid[i][j];
                    ans++;
                }
            }
            if(pre==1){
                pre=0;
                ans++;
            }
        }
        return ans;
            
    }
};