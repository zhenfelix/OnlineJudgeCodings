class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m=matrix.size();
        if(m==0)return 0;
        int n=matrix[0].size(),ans=0;
        vector<vector<int>> square(m,vector<int>(n,0));
        for(int j=n-1;j>=0;j--){square[m-1][j]=(matrix[m-1][j]=='1'?1:0);ans=max(ans,square[m-1][j]);}
        for(int i=m-1;i>=0;i--){square[i][n-1]=(matrix[i][n-1]=='1'?1:0);ans=max(ans,square[i][n-1]);}
        for(int i=m-2;i>=0;i--){
            for(int j=n-2;j>=0;j--){
                if(matrix[i][j]=='0')square[i][j]=0;
                else square[i][j]=min(min(square[i+1][j],square[i][j+1]),square[i+1][j+1])+1;
                ans=max(ans,square[i][j]);
            }
        }
        
        return ans*ans;
    }
};