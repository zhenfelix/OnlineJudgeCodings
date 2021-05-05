class Solution {
public:
    int findTheWinner(int n, int k) {
        int dp = 0;
        for (int t = 2; t <= n; ++t)
        {
            dp += k;
            dp %= t;
        }
        return dp+1;
    }
};