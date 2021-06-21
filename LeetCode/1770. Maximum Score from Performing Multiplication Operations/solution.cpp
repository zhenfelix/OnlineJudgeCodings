class Solution {
public:
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        int n = nums.size(), m = multipliers.size();
        vector<int> dp(m+1, 0);
        for (int k = 1; k <= m; k++){
            dp[k] = dp[k-1] + nums[k-1]*multipliers[k-1];
            for (int i = k-1; i > 0; i--){
                dp[i] = max(dp[i-1]+nums[i-1]*multipliers[k-1],dp[i]+nums[n+i-k]*multipliers[k-1]);
            }
            dp[0] = dp[0] + nums[n-k]*multipliers[k-1];
        }
        return *max_element(dp.begin(), dp.end());
    }
};
