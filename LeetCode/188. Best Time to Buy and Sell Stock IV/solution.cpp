
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        vector<int> cash(k+1,0), hold(k+1,0xc0c0c0c0);
        for(int p: prices){
            for(int i=k;i>0;i--){
                cash[i] = max(cash[i], hold[i]+p);
                hold[i] = max(hold[i], cash[i-1]-p);
            }
        }
        return *max_element(cash.begin(),cash.end());
    }
};