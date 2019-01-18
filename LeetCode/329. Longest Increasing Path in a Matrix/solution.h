class Solution {


public:
    vector<int> dx{0,0,-1,1};
    vector<int> dy{-1,1,0,0};
    int dfs(vector<vector<int>>& matrix, vector<vector<int>>& ans, int i, int j){
        if(ans[i][j]>0)return ans[i][j];
        int tmp=0;
        int m=matrix.size();
        int n=matrix[0].size();
        for(int k=0;k<4;k++){
            int x=dx[k],y=dy[k];
            if(i+x>=0&&i+x<m&&j+y>=0&&j+y<n&&matrix[i][j]<matrix[i+x][j+y])tmp=max(tmp,dfs(matrix,ans,i+x,j+y));
        }
        ans[i][j]=tmp+1;
        return ans[i][j];
    }
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m=matrix.size();
        if(m==0)return 0;
        int n=matrix[0].size();
        vector<vector<int>> ans(m,vector<int>(n,0));
        int max_ans=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                max_ans=max(max_ans,dfs(matrix,ans,i,j));
            }
        }
        return max_ans;
    }
};