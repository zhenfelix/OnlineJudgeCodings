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


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> ready(2,0), hold(2,0), sell(2,0);
        int n = prices.size();
        for(int i=0;i<n;i++){
            int idx = i&1;
            ready[idx] = max(ready[idx^1],sell[idx^1]);
            hold[idx] = ready[idx^1];
            if(i>0)hold[idx] = max(hold[idx], hold[idx^1]+prices[i]-prices[i-1]);
            sell[idx] = hold[idx];
        }
        return max(sell[(n-1)&1],ready[(n-1)&1]);
    }
};