class Solution {
public:
    string stoneGameIII(vector<int>& stoneValue) {
        int n = stoneValue.size();
        vector<int> dp(n+1, INT_MIN);
        dp.back() = 0;
        for (int i = n-1; i >= 0; i--){
            int sums = 0;
            for (int j = i; j < i+3 && j < n; j++){
                sums += stoneValue[j];
                dp[i] = max(dp[i], sums-dp[j+1]);
            }
        }
        return dp[0] == 0 ? "Tie" : dp[0] > 0 ? "Alice" : "Bob";
    }
};