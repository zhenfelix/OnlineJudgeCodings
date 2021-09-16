class Solution {
private:
    static constexpr int mod = 1000000007;
    using LL = long long;
    
public:
    // 快速幂，用来计算 x^y mod m
    int quickmul(int x, int y) {
        int ret = 1, mul = x;
        while (y) {
            if (y & 1) {
                ret = (LL)ret * mul % mod;
            }
            mul = (LL)mul * mul % mod;
            y >>= 1;
        }
        return ret;
    }
    
    int makeStringSorted(string s) {
        int n = s.size();
        
        // fac[i] 表示 i! mod m
        // facinv[i] 表示 i! 在 mod m 意义下的乘法逆元
        vector<int> fac(n + 1), facinv(n + 1);
        fac[0] = facinv[0] = 1;
        for (int i = 1; i < n; ++i) {
            fac[i] = (LL)fac[i - 1] * i % mod;
            // 使用费马小定理 + 快速幂计算乘法逆元
            facinv[i] = quickmul(fac[i], mod - 2);
        }
        
        // freq 存储每个字符出现的次数
        vector<int> freq(26);
        for (char ch: s) {
            ++freq[ch - 'a'];
        }
        
        int ans = 0;
        for (int i = 0; i < n - 1; ++i) {
            // rank 求出比 s[i] 小的字符数量
            int rank = 0;
            for (int j = 0; j < s[i] - 'a'; ++j) {
                rank += freq[j];
            }
            // 排列个数的分子
            int cur = (LL)rank * fac[n - i - 1] % mod;
            // 依次乘分母每一项阶乘的乘法逆元
            for (int j = 0; j < 26; ++j) {
                cur = (LL)cur * facinv[freq[j]] % mod;
            }
            ans = (ans + cur) % mod;
            --freq[s[i] - 'a'];
        }
        
        return ans;
    }
};






using ll = long long;
const int maxn = 3005;
const int MOD = 1e9 + 7;
vector<ll> fac(maxn, 1), ifac(maxn, 1);
bool initialized = false;

class Solution
{
public:
    ll quickmul(ll a, ll q)
    {
        ll res = 1;
        while (q)
        {
            if (q & 1)
            {
                res *= a;
                res %= MOD;
            }
            q >>= 1;
            a *= a;
            a %= MOD;
        }
        return res;
    }
    void init()
    {
        for (int i = 1; i < maxn; i++)
        {
            fac[i] = fac[i - 1] * i;
            fac[i] %= MOD;
        }
        ifac[maxn - 1] = quickmul(fac[maxn - 1], MOD - 2);
        for (int i = maxn - 2; i >= 1; i--)
        {
            ifac[i] = ifac[i + 1] * (i + 1);
            ifac[i] %= MOD;
        }
        initialized = true;
    }
    int makeStringSorted(string s)
    {
        if (!initialized)
            init();
        int n = s.length(), sums = 0;
        ll res = 0;
        vector<int> cnt(26, 0);
        for (int i = n - 1; i >= 0; i--)
        {
            // int rank = s[i] - 'a';
            // for (int j = 0; j < rank; j++)
            // {
            //     if (cnt[j] == 0)
            //         continue;
            //     cnt[j]--;
            //     cnt[rank]++;
            //     ll tmp = fac[sums];
            //     for (int k = 0; k < 26; k++)
            //     {
            //         tmp *= ifac[cnt[k]];
            //         tmp %= MOD;
            //     }
            //     res += tmp;
            //     res %= MOD;
            //     cnt[j]++;
            //     cnt[rank]--;
            // }
            // cnt[rank]++;sums++;
            cnt[s[i]-'a']++;sums++;
            int rank = 0;
            for (int j = 0; 'a'+j < s[i]; j++)
                rank += cnt[j];
            ll tmp = rank*fac[sums-1]%MOD;
            for (int j = 0; j < 26; j++){
                tmp *= ifac[cnt[j]];
                tmp %= MOD;
            }
            res += tmp;
            res %= MOD;

        }
        return res;
    }
};




class Solution {
public:
    #define ll long long
    #define N 3005
    #define mod 1000000007
    int f[N];
    int exp(int a,int n) 
    {
        int r=1;
        for (;n; n>>=1) {
            if (n&1) r=(ll)r*a%mod;
            a=(ll)a*a%mod;
        }
        return r;
    }
    int makeStringSorted(string s) {
        int n=s.size();
        f[0]=1;
        for (int i=1;i<=n;i++) {
            f[i]=(ll)i*f[i-1]%mod;
        }
        //  return 0;
        vector<int> z(26, 0);
        for (int i=0;i<n;i++)z[s[i]-'a']++;
        int ans=0,p=1;
        for (int i=0;i<26;i++) p=(ll)p*exp(f[z[i]],mod-2)%mod;
        for (int i=0;i<n;i++) {
            int cur=s[i]-'a';
            int r=0;
            for (int t=0;t<cur;t++) r+=z[t];
            ans=(ans+(ll)r*f[n-i-1]%mod*p)%mod;
            p=(ll)p*z[cur]%mod; 
            --z[cur];
        }
        return ans;
    }
};
