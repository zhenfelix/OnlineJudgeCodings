

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
    int m = matrix.size();
    if (m == 0) return false;
    int n = matrix[0].size();

    int i = 0, j = n - 1;
    while (i < m && j >= 0) {
        if (matrix[i][j] == target)
            return true;
        else if (matrix[i][j] > target) {
            j--;
        } else 
            i++;
    }
    return false;
}
};