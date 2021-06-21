// class Solution {
// public:
//     int longestPalindrome(string word1, string word2) {
//         int n = word1.size(), m = word2.size();
//         vector<vector<int>> dp1(n, vector<int>(n,0));
//         vector<int> left1(26, INT_MAX);
//         for (int i = n-1; i >= 0; i--){
//             dp1[i][i] = 1;
//             left1[word1[i]-'a'] = i;
//             for (int j = i+1; j < n; j++){
//                 dp1[i][j] = dp1[i][j-1];
//                 int idx = left1[word1[j]-'a'];
//                 if (idx < j){
//                     dp1[i][j] = max(dp1[i][j], dp1[idx+1][j-1]+2);
//                 }
//             }
//         }
//         vector<vector<int>> dp2(m, vector<int>(m,0));
//         vector<int> left2(26, INT_MAX);
//         for (int i = m-1; i >= 0; i--){
//             dp2[i][i] = 1;
//             left2[word2[i]-'a'] = i;
//             for (int j = i+1; j < m; j++){
//                 dp2[i][j] = dp2[i][j-1];
//                 int idx = left2[word2[j]-'a'];
//                 if (idx < j){
//                     dp2[i][j] = max(dp2[i][j], dp2[idx+1][j-1]+2);
//                 }
//             }
//         }
//         int res = 0;
//         vector<vector<int>> dp(n, vector<int>(m,0));
//         vector<int> left(26, INT_MAX);
//         for (int i = n-1; i >= 0; i--){
//             left[word1[i]-'a'] = i;
//             dp[i][0] = dp1[i][n-1];
//             int idx = left[word2[0]-'a'];
//             if (idx < INT_MAX){
//                 int len = (idx < n-1 ? dp1[idx+1][n-1] : 0) + 2;
//                 res = max(res, len);
//                 dp[i][0] = max(dp[i][0], len);
//             }
//             else{
//                 dp[i][0] = max(dp[i][0], 1);
//             }
//             for (int j = 1; j < m; j++){
//                 dp[i][j] = dp[i][j-1];
//                 int idx = left[word2[j]-'a'];
//                 if (idx < INT_MAX){
//                     int len = (idx < n-1 ? dp[idx+1][j-1] : dp2[0][j-1]) + 2;
//                     res = max(res, len);
//                     dp[i][j] = max(dp[i][j], len);
//                 }
//                 else{
//                     dp[i][j] = max(dp[i][j], dp2[0][j]);
//                 }
//             }
//         }
//         return res;
//     }
// };



class Solution {
public:
    int longestPalindrome(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        auto word = word1 + word2;
        vector<vector<int>> dp(n+m, vector<int>(n+m,0));
        int res = 0;
        for (int i = n+m-1; i >= 0; i--){
            dp[i][i] = 1;
            for (int j = i+1; j < n+m; j++){
                dp[i][j] = max(dp[i][j-1], dp[i+1][j]);
                if (word[i] == word[j]){
                    int len = dp[i+1][j-1] + 2;
                    if (i < n && j >= n){
                        res = max(res, len);
                    }
                    dp[i][j] = max(dp[i][j], len);
                }
                
            }
        }
        
        return res;
    }
};