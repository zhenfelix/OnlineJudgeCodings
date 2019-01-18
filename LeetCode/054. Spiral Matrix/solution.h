// class Solution {
// public:
//     vector<int> spiralOrder(vector<vector<int> >& matrix) {
//         if(matrix.empty())return {};
//         int k = 0, i = 0;
//         int n=matrix.size();
//         int m=matrix[0].size();
        
//         vector<int> ans(n*m);
//          while( k < n * m )
//          {
                
//              int j = i;
                
//                     // four steps
//              while( j < m - i && k < n * m)   {          // 1. horizonal, left to right
//                  ans[k++]=matrix[i][j++];}
//              j = i + 1;
//              while( j < n - i && k < n * m)             // 2. vertical, top to bottom
//                  ans[k++]=matrix[j++][m-i-1];
//              j = m - i - 2;
//              while( j > i && k < n * m)                  // 3. horizonal, right to left 
//                  ans[k++]=matrix[n-i-1][j--];
//              j = n - i - 1;
//              while( j > i && k < n * m)                  // 4. vertical, bottom to  top 
//                  ans[k++]=matrix[j--][i];
//              i++;      // next loop
//          }
//          return ans;
//     }
// };

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int> >& matrix) {
        if(matrix.empty())return {};
        int k = 0, i = 0, j = 0;
        int n=matrix.size();
        int m=matrix[0].size();
        vector<vector<bool>> visit(n, vector<bool>(m,false));
        vector<int> ans(n*m);
        while( k < n * m )
        {
            
            // int j = i;
            
            // four steps
            while( j < m  && k < n * m && visit[i][j]==false)   {          // 1. horizonal, left to right
                visit[i][j]=true;ans[k++]=matrix[i][j++];}
            j--;i++;
            while( i < n  && k < n * m && visit[i][j]==false){              // 2. vertical, top to bottom
                visit[i][j]=true;ans[k++]=matrix[i++][j];
            }
            i--;j--;
            while( j >= 0 && k < n * m && visit[i][j]==false)                  // 3. horizonal, right to left
            {visit[i][j]=true;ans[k++]=matrix[i][j--];}
            i--;j++;
            while( i >= 0 && k < n * m  && visit[i][j]==false)                  // 4. vertical, bottom to  top
            {visit[i][j]=true;ans[k++]=matrix[i--][j];}
            i++;j++;     // next loop
        }
        return ans;
    }
};


// class Solution {
// public:
//     vector<int> spiralOrder(vector<vector<int>>& matrix) {
//         if (matrix.empty()) return {};
//         int m = matrix.size(), n = matrix[0].size();
//         vector<int> spiral(m * n);
//         int u = 0, d = m - 1, l = 0, r = n - 1, k = 0;
//         while (true) {
//             // up
//             for (int col = l; col <= r; col++) spiral[k++] = matrix[u][col];
//             if (++u > d) break;
//             // right
//             for (int row = u; row <= d; row++) spiral[k++] = matrix[row][r];
//             if (--r < l) break;
//             // down
//             for (int col = r; col >= l; col--) spiral[k++] = matrix[d][col];
//             if (--d < u) break;
//             // left
//             for (int row = d; row >= u; row--) spiral[k++] = matrix[row][l];
//             if (++l > r) break;
//         }
//         return spiral;
//     }
// };