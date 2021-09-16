using ll = long long;

const int MOD = 1e9 + 7;
const int maxn = 10020;
vector<ll> fac(maxn, 1), ifac(maxn, 1);
bool initialized = false;

class Solution
{
public:
    ll qucikmul(ll a, ll q)
    {
        ll res = 1;
        while (q)
        {
            if (q & 1)
                res = (res * a) % MOD;
            q >>= 1;
            a = (a * a) % MOD;
        }
        return res;
    }
    void init()
    {
        for (int i = 1; i < maxn; i++)
            fac[i] = (i * fac[i - 1]) % MOD;
        ifac[maxn - 1] = qucikmul(fac[maxn - 1], MOD - 2);
        for (int i = maxn - 2; i >= 1; i--)
            ifac[i] = ((i + 1) * ifac[i + 1]) % MOD;
        initialized = true;
    }
    vector<int> waysToFillArray(vector<vector<int>> &queries)
    {
        if (!initialized)
            init();
        vector<int> ans;
        for (auto query : queries)
        {
            int n = query[0], k = query[1], i = 2, cnt;
            ll res = 1;
            while ((k > 1) && (i <= k))
            {
                if ((k % i) == 0)
                {
                    cnt = 0;
                    while ((k % i) == 0)
                    {
                        cnt++;
                        k /= i;
                    }
                    res *= fac[cnt+n-1];
                    res %= MOD;
                    res *= ifac[cnt];
                    res %= MOD;
                    res *= ifac[n-1];
                    res %= MOD;
                }
                i++;
                
            }
            if (k > 1)
                res = (res * n) % MOD;
            ans.push_back(res);
        }
        return ans;
    }
};



using LL = long long;

class Solution {
private:
    static constexpr int mod = 1000000007;
    static constexpr int nmax = 10000;
    static constexpr int logkmax = 13;
    static int c[nmax + logkmax][logkmax + 1];
    static bool inited;
    
    vector<int> factors;
    int n, k;
    int sum;
    int u;
    
public:
    // 预处理组合数
    void init() {
        if (inited) {
            return;
        }
        inited = true;
        
        c[0][0] = 1;
        for (int i = 1; i < nmax + logkmax; ++i) {
            c[i][0] = 1;
            for (int j = 1; j <= i && j <= logkmax; ++j) {
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
                if (c[i][j] >= mod) {
                    c[i][j] -= mod;
                }
            }
        }
    }
    
    vector<int> waysToFillArray(vector<vector<int>>& queries) {
        init();
        
        vector<int> ans;
        for (const auto& q: queries) {
            int n = q[0], k = q[1];
            int sum = 1;
            for (int i = 2; i * i <= k; ++i) {
                if (k % i == 0) {
                    int y = 0;
                    while (k % i == 0) {
                        ++y;
                        k /= i;
                    }
                    sum = (LL)sum * c[n + y - 1][y] % mod;
                }
            }
            if (k != 1) {
                sum = (LL)sum * n % mod;
            }
            ans.push_back(sum);
        }
        return ans;
    }
};

int Solution::c[nmax + logkmax][logkmax + 1] = {0};
bool Solution::inited = false;


作者：zerotrac2
链接：https://leetcode-cn.com/problems/count-ways-to-make-array-with-product/solution/sheng-cheng-cheng-ji-shu-zu-de-fang-an-s-rmso/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    vector<int> waysToFillArray(vector<vector<int>>& queries) {
        int sz = queries.size();

        const int mod = 1e9+7;
        const int maxc = 15;
        int maxn = 0, maxk = 0;
        for (int i = 0; i < sz; i++) {
            maxn = max(maxn, queries[i][0]);
            maxk = max(maxk, queries[i][1]);
        }
        
        vector<vector<int>> dp(maxn + 1, vector<int>(maxc + 1, 0));
        for (int i = 1; i <= maxc; i++) {
            dp[1][i] = 1;
        }
        for (int i = 1; i <= maxn; i++) {
            dp[i][0] = 1;
        }
        for (int i = 2; i <= maxn; i++) {
            for (int j = 1; j <= maxc; j++) {
                for (int k = 0; k <= j; k++) {
                    dp[i][j] += dp[i - 1][j - k];
                    dp[i][j] %= mod;
                }
            }
        }

        vector<int> isPrime(maxk + 1, 1);
        vector<int> primes;
        for (int i = 2; i <= maxk; i++) {
            if (isPrime[i] == 1) {
                primes.push_back(i);
            }
            for (int j = i * 2; j <= i * i && j <= maxk; j += i) {
                isPrime[j] = 0;
            }
        }

        vector<int> ret(sz);
        for (int i = 0; i < sz; i++) {
            int n = queries[i][0], k = queries[i][1];

            vector<int> cs;
            for (int p: primes) {
                if (p > k) {
                    break;
                }
                int cnt = 0;
                int left = k;
                while (left % p == 0) {
                    left /= p;
                    cnt++;
                }
                if (cnt > 0) {
                    cs.push_back(cnt);
                }
            }

            long long ans = 1;
            for (int c: cs) {
                ans *= dp[n][c];
                ans %= mod;
            }
            ret[i] = ans;
        }
        return ret;
    }
};


作者：Arsenal-591
链接：https://leetcode-cn.com/problems/count-ways-to-make-array-with-product/solution/dong-tai-gui-hua-xu-yao-yi-dian-dian-shu-2w2d/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


