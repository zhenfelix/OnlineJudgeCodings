using ll = long long;
class Solution {
public:
    int countOrders(int n) {
        int res = 1, MOD = 1e9+7;
        for (int i = 2; i <= n; i++)
            res = ((ll)res*i*(2*i-1))%MOD;
        return res;
    }
};