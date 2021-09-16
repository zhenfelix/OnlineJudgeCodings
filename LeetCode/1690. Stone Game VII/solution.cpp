class Solution {
public:
    int stoneGameVII(vector<int>& stones) {
        int n = stones.size();
        vector<int> dp(n,0), presums = {0};
        for (auto s : stones)
            presums.push_back(presums.back()+s);
        
        for (int i = n-1; i >= 0; i--){
            for (int j = i+1; j < n; j++){
                dp[j] = max(presums[j]-presums[i]-dp[j-1], presums[j+1]-presums[i+1]-dp[j]);
            }
        }
        return dp.back();

    }
};