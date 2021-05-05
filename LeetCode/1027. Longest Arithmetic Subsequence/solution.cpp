class Solution {
public:

    
    int longestArithSeqLength(vector<int>& A) {
        int res = 0, mi = *min_element(A.begin(),A.end()), mx = *max_element(A.begin(),A.end());
        
        for (int delta = mi-mx; delta <= mx-mi; ++delta)
        {
            vector<int> dp(1010,0);
            for (auto &a : A)
            {
                if (a-delta >= 0 && a-delta < 1010)
                    dp[a] = dp[a-delta] + 1;
                else
                    dp[a] = 1;
                res = max(res, dp[a]);
            }
        }
        return res;
    }
};

// class Solution
// {
// public:

//     int longestArithSeqLength(vector<int> &A)
//     {
//         int res = 1, n = A.size();
//         // vector<unordered_map<int, int>> dp(n);
//         vector<vector<int>> dp(n,vector<int>(2000,1));
//         for (int i = 0; i < n; i++)
//         {

//             for (int j = 0; j < i; j++)
//             {
//                 int delta = A[i] - A[j] + 1000;
//                 dp[i][delta] = max(dp[i][delta], 1 + dp[j][delta]);
//                 res = max(res, dp[i][delta]);
//             }
//         }
//         return res;
//     }
// };