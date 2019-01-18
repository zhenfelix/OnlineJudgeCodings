// class Solution {
// public:
//     void loop(int i,int j,int L,vector<vector<int>> &matrix){
//         vector<int> x{i,i+j,i+L-1,i+L-1-j},y{i+j,i+L-1,i+L-1-j,i};
//         int tmp=matrix[x[3]][y[3]];
//         int t=3;
//         for(;t>0;t--)matrix[x[t]][y[t]]=matrix[x[t-1]][y[t-1]];
//         matrix[x[t]][y[t]]=tmp;
//     }
//     void rotate(vector<vector<int>>& matrix) {
//         int n=matrix.size();
//         for(int i=0;i<n/2;i++){
//             int L=n-i*2;
//             for(int j=0;j<L-1;j++)loop(i,j,L,matrix);
//         }
//         return;
//     }
// };

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        
        for(int i = 0; i < n; i++){
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};