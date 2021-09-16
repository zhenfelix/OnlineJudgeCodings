#define LL long long

class Fancy {
private:
    vector<LL> nums;
    LL add, mul;
    const int mod = 1000000007;
    
    LL power(LL x, int y) {
        LL tot = 1, p = x;
        for (; y; y >>= 1) {
            if (y & 1)
                tot = (tot * p) % mod;
            p = (p * p) % mod;
        }
        return tot;
    }

public:
    Fancy() {
        add = 0;
        mul = 1;
    }
    
    void append(int val) {
        val = ((val - add) % mod + mod) % mod;
        val = (val * power(mul, mod - 2)) % mod;
        nums.push_back(val);
    }
    
    void addAll(int inc) {
        add = (add + inc) % mod;
    }
    
    void multAll(int m) {
        add = add * m % mod;
        mul = mul * m % mod;
    }
    
    int getIndex(int idx) {
        if (idx >= nums.size())
            return -1;
        return (nums[idx] * mul + add) % mod;
    }
};

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy* obj = new Fancy();
 * obj->append(val);
 * obj->addAll(inc);
 * obj->multAll(m);
 * int param_4 = obj->getIndex(idx);
 */



using ll = long long;

const int MOD = 1e9+7;

class Fancy {
public:
    vector<ll> ks, bs, nums;
    ll k, b;
    Fancy() {
        k = 1, b = 0;
    }
    
    void append(int val) {
        nums.push_back(val);
        ks.push_back(k);
        bs.push_back(b);
    }
    
    void addAll(int inc) {
        b = (b + inc)%MOD;
    }
    
    void multAll(int m) {
        b = (b*m)%MOD;
        k = (k*m)%MOD;
    }
    
    int getIndex(int idx) {
        if (idx >= nums.size())
            return -1;
        ll k_ = (k*quickmul(ks[idx],MOD-2))%MOD;
        ll b_ = (b - (k_*bs[idx])%MOD + MOD)%MOD;
        return (nums[idx]*k_+b_)%MOD;
    }

    int quickmul(int a, int p){
        int res = 1;
        while (p){
            if (p&1)
                res = ((ll)res*a)%MOD;
            a = ((ll)a*a)%MOD;
            p >>= 1;
        }
        return res;
    }
};

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy* obj = new Fancy();
 * obj->append(val);
 * obj->addAll(inc);
 * obj->multAll(m);
 * int param_4 = obj->getIndex(idx);
 */