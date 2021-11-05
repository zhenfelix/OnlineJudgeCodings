const int inf = 0x3f3f3f3f;
class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        vector<vector<int>> dp(n+1,vector<int>(m+1,0));
        int res = -inf;
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= m; j++){
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                dp[i][j] = max(dp[i][j], nums1[i-1]*nums2[j-1]+dp[i-1][j-1]);
                res = max(res, nums1[i-1]*nums2[j-1]+dp[i-1][j-1]);
                // cout << i << " " << j << " " << dp[i][j] << endl;
            }
        }
        return res;
    }
};


class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int i, j, m = nums1.size(), n = nums2.size();
        vector<vector<int>> dp(m+1, vector<int>(n+1,INT_MIN));
        // dp[i][j] 表示截至nums1第i个数，nums2第j个数的最大点积
        for(i = 1; i <= m; ++i)
        {
            for(j = 1; j <= n; ++j)
            {
                if(dp[i-1][j-1] > 0)
                    dp[i][j] = max(dp[i-1][j-1]+nums1[i-1]*nums2[j-1] ,max(dp[i-1][j],dp[i][j-1]));
                else
                    dp[i][j] = max(nums1[i-1]*nums2[j-1] ,max(dp[i-1][j],dp[i][j-1]));
            }
        }
        return dp[m][n];
    }
};
