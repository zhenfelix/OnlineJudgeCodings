class Solution {
public:
    vector<int> solve(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), MOD = 1000000007;
        int sq = sqrt(n);
        vector<vector<int>> dp;
        dp.emplace_back(nums.begin(), nums.end());
        for (int len = 1; len <= sq; len++){
            dp.emplace_back(nums.begin(), nums.end());
            for (int i = n-1; i > n-1-len; i--){
                for (int j = i; j >= 0; j -= len){
                    if (j-len >= 0){
                        dp[len][j-len] += dp[len][j];
                        dp[len][j-len] %= MOD;
                    }
                }
            }
        }
        vector<int> res;
        for (auto &item : queries){
            int x = item[0], y = item[1];
            int cur = 0;
            if (y <= sq){
                cur = dp[y][x];
            }
            else{
                for (int i = x; i < n; i += y){
                    cur += nums[i];
                    cur %= MOD;
                }
            }
            res.emplace_back(cur%MOD);
        }
        return res;
    }
};