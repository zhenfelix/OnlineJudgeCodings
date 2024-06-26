#include <vector>
#include <string>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        for(int i=1;i<prices.size();i++){
            int delta = prices[i]-prices[i-1];
            if(delta>0)profit += delta;
        }
        return profit;
    }
};
