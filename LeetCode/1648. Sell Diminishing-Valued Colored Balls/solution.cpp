using ll = long long;

class Solution {
public:
    int maxProfit(vector<int>& inventory, int orders) {
        sort(inventory.begin(), inventory.end(), greater<>());
        inventory.push_back(0);
        ll sums = 0, pre = inventory[0];
        int MOD = 1e9+7, n = inventory.size(); 
        for (int i = 1; i < n && orders; i++){
            if (inventory[i] < pre){
                if (i*(pre-inventory[i]) <= orders){
                    sums += i*(pre+inventory[i]+1)*(pre-inventory[i])/2;
                    orders -= i*(pre-inventory[i]);
                    pre = inventory[i];
                }
                else{
                    int k = orders/i, r = orders%i;
                    sums += i*(pre+pre-k+1)*k/2;
                    pre -= k;
                    sums += r*pre;
                    orders = 0;
                }
                sums %= MOD;
                // cout << sums << " " << i <<  " " << orders << endl;
            }
        }
        return sums;

    }
};