class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int res = 0;
        sort(costs.begin(),costs.end());
        for (auto x : costs)
        {
            if (x > coins)
                break;
            res++;
            coins -= x;
        }
        return res;
    }
};