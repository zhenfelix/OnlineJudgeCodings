const int MOD = 1e9+7;
using ll = long long;

ll quickmul(ll a, ll p){
    ll res = 1;
    while (p){
        if (p&1)
            res = res*a%MOD;
        p >>= 1;
        a = a*a%MOD;
    }
    return res;
}

class Solution {
public:
    int maxNiceDivisors(int primeFactors) {
        if (primeFactors <= 4)
            return primeFactors;
        int r = primeFactors%3, k = primeFactors/3;
        int m = 1;
        if (r == 1)
            m = 4, k--;
        else if (r == 2)
            m = 2;
        ll res = quickmul(3,k);
        return res*m%MOD;
    }
};