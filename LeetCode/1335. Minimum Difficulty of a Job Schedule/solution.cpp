// const int inf = 0x3f3f3f3f;
// class Solution {
// public:
//     int minDifficulty(vector<int>& jobDifficulty, int d) {
//         int n = jobDifficulty.size();
//         if (d > n)
//             return -1;
//         vector<vector<int>> dp(d+1, vector<int>(n+1,inf));
//         dp[0][0] = 0;
//         for (int i = 1; i <= d; i++){
//             for (int j = i; j <= n; j++){
//                 int mx = 0;
//                 for (int k = j; k >= i; k--){
//                     mx = max(mx, jobDifficulty[k-1]);
//                     dp[i][j] = min(dp[i][j], dp[i-1][k-1]+mx);
//                 }
//             }
//         }
//         return dp[d][n];
//     }
// };



const int inf = 0x3f3f3f3f;
class Solution {
public:
    int minDifficulty(vector<int>& jobDifficulty, int d) {
        int n = jobDifficulty.size();
        if (d > n)
            return -1;
        vector<vector<int>> dp(d+1, vector<int>(n+1,inf));
        dp[0][0] = 0;
        for (int i = 1; i <= d; i++){
            vector<int> mx,midp;

            for (int j = i; j <= n; j++){
                while (!mx.empty() && jobDifficulty[mx.back()-1] <= jobDifficulty[j-1])
                    mx.pop_back();
                int k = mx.empty() ? i-1 : mx.back();
                mx.push_back(j);
                while (!midp.empty() && dp[i-1][midp.back()-1] >= dp[i-1][j-1])
                    midp.pop_back();
                midp.push_back(j);
                int kk = *upper_bound(midp.begin(), midp.end(), k);
                dp[i][j] = min(dp[i][k], dp[i-1][kk-1]+jobDifficulty[j-1]);
                
                // int mx = 0;
                // for (int k = j; k >= i; k--){
                //     mx = max(mx, jobDifficulty[k-1]);
                //     dp[i][j] = min(dp[i][j], dp[i-1][k-1]+mx);
                // }
                // cout << i << " " << j << " " << k << " " << dp[i][j] << endl;
                // for (auto x : midp)
                //     cout << x << " ";
                // cout << endl;
            }
            // cout << endl;
        }
        return dp[d][n];
    }
};








const int inf = 0x3f3f3f3f;
class Solution {
public:
    int minDifficulty(vector<int>& jobDifficulty, int d) {
        int n = jobDifficulty.size();
        if (d > n)
            return -1;
        vector<vector<int>> dp(d+1, vector<int>(n+1,inf));
        dp[0][0] = 0;
        for (int i = 1; i <= d; i++){
            vector<int> mx;

            for (int j = i; j <= n; j++){
                while (!mx.empty() && jobDifficulty[mx.back()-1] <= jobDifficulty[j-1]){
                    dp[i-1][j-1] = min(dp[i-1][j-1], dp[i-1][mx.back()-1]);
                    mx.pop_back();
                }
                int k = mx.empty() ? i-1 : mx.back();
                mx.push_back(j);
                dp[i][j] = min(dp[i][k], dp[i-1][j-1]+jobDifficulty[j-1]);      
            }
        }
        return dp[d][n];
    }
};


// 作者：Arsenal-591
// 链接：https://leetcode-cn.com/problems/minimum-difficulty-of-a-job-schedule/solution/ond-dong-tai-gui-hua-dan-diao-zhan-you-hua-by-arse/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。