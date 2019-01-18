class Solution {
public:
    int maxProfit(vector<int>& prices){
        int n=prices.size();
        if (n <= 1) return 0;
        vector<int> rest(n, 0);
        vector<int> hold(n, 0);
        vector<int> sell(n, 0);
        hold[1] = max(-prices[0], -prices[1]);
        rest[1] = 0;
        sell[1] = prices[1]-prices[0];
        for (int i = 2; i < n; i++) {
            rest[i] = max(rest[i - 1], sell[i - 1]);
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i]);
            sell[i] = hold[i - 1] + prices[i];
        }
        return max(rest[n - 1], sell[n - 1]);
    }
};