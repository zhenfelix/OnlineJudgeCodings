// class Solution {
// public:
//     bool dp(vector<vector<int>> &mat, int target, int row, int col){
//         if(row==mat.size()||col==-1)return false;
//         if(mat[row][col]==target)return true;
//         else if(mat[row][col]>target)return dp(mat, target, row, col-1);
//         else return dp(mat, target, row+1, col);
        
//     }
//     bool searchMatrix(vector<vector<int>>& matrix, int target) {
//         if(matrix.size()>0)return dp(matrix, target, 0, matrix[0].size()-1);
//         return false;
//     }
// };


class Solution {
public:

    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m,n,mid,left,right;
        m=matrix.size();
        if(m==0)return false;
        n=matrix[0].size();
        left=0;right=m*n-1;
        while(left<=right){
            mid=(left+right)/2;
            if(matrix[mid/n][mid%n]==target)return true;
            else if(matrix[mid/n][mid%n]<target)left=mid+1;
            else right=mid-1;
            
        }
        return false;
    }
};