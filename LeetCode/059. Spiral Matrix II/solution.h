class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n, vector<int>(n,0));
        int i=0,j=0,v=1;
        while(v<=n*n){
            while(j<n && ans[i][j]==0){
                ans[i][j++]=v++;
            }
            j--;i++;
            while(i<n && ans[i][j]==0){
                ans[i++][j]=v++;
            }
            i--;j--;
            while(j>=0 && ans[i][j]==0){
                ans[i][j--]=v++;
            }
            j++;i--;
            while(i>=0 && ans[i][j]==0){
                ans[i--][j]=v++;
            }
            i++;j++;
        }
        return ans;
    }
};