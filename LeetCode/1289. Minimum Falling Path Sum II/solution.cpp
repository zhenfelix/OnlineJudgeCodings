// const int inf = 0x3f3f3f3f;
// class Solution {
// public:
//     int minFallingPathSum(vector<vector<int>>& grid) {
//         int n = grid.size(), m = grid[0].size();
//         vector<vector<int>> dp(n,vector<int>(m,inf));
//         for (int j = 0; j < m; j++)
//             dp[0][j] = grid[0][j];
//         for (int i = 1; i < n; i++){
//             int pre = inf;
//             for (int j = 0; j < m; j++){
//                 dp[i][j] = min(dp[i][j],pre);
//                 pre = min(pre,dp[i-1][j]);
//             }
//             pre = inf;
//             for (int j = m-1; j >= 0; j--){
//                 dp[i][j] = min(dp[i][j],pre);
//                 pre = min(pre,dp[i-1][j]);
//             }
//             for (int j = 0; j < m; j++){
//                 dp[i][j] += grid[i][j];
//             }
//         }
//         return *min_element(dp[n-1].begin(), dp[n-1].end());
//     }
// };


class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& arr) {
        int n = arr.size();
        int first_sum = 0, first_pos = -1, second_sum = 0;
        for (int i = 0; i < n; ++i) {
            int fs = INT_MAX, fp = -1, ss = INT_MAX;
            for (int j = 0; j < n; ++j) {
                int cur_sum = (first_pos != j ? first_sum : second_sum) + arr[i][j];
                if (cur_sum < fs) {
                    ss = fs;
                    fs = cur_sum;
                    fp = j;
                }
                else if (cur_sum < ss) {
                    ss = cur_sum;
                }
            }
            first_sum = fs;
            first_pos = fp;
            second_sum = ss;
        }
        return first_sum;
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/minimum-falling-path-sum-ii/solution/xia-jiang-lu-jing-zui-xiao-he-ii-by-leetcode-solut/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。