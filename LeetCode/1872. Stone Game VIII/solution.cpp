// class Solution {
// public:
//     int stoneGameVIII(vector<int>& stones) {
//         vector<int> sums(stones.begin(), stones.end());
//         int n = stones.size();
//         for (int i = 1; i < n; i++)
//             sums[i] += sums[i-1];
//         vector<int> dp(n+1);
//         dp[n] = 0;
//         int g = INT_MIN;
//         for (int i = n-1; i >= 0; i--){
//             g = max(g, sums[i]-dp[i+1]);
//             dp[i] = g;
//         }
//         return dp[1];
//     }
// };

// class Solution {
// public:
//     int stoneGameVIII(vector<int>& stones) {
//         vector<int> sums(stones.begin(), stones.end());
//         int n = stones.size();
//         for (int i = 1; i < n; i++)
//             sums[i] += sums[i-1];
//         int dp = 0;
//         int g = INT_MIN;
//         for (int i = n-1; i > 0; i--){
//             g = max(g, sums[i]-dp);
//             dp = g;
//         }
//         return dp;
//     }
// };

class Solution {
public:
    int stoneGameVIII(vector<int>& stones) {
        int sums = 0, n = stones.size();
        for (int i = 0; i < n; i++)
            sums += stones[i];
        int dp = 0, g = INT_MIN;
        for (int i = n-1; i > 0; i--){
            g = max(g, sums-dp);
            dp = g;
            sums -= stones[i];
        }
        return dp;
    }
};