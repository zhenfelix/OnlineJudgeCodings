class Solution {
    const int MOD = 1000000007;
    const int MAXP = 16;

public:
    int idealArrays(int n, int K) {
        // nlnn 求因数
        vector<vector<int>> fac(K + 1);
        for (int i = 1; i <= K; i++) for (int j = i << 1; j <= K; j += i) fac[j].push_back(i);

        // 计算子问题的答案
        vector<vector<long long>> f;        
        f.resize(K + 1, vector<long long>(20));
        for (int i = 1; i <= K; i++) {
            f[i][1] = 1;
            for (int j = 2; j <= MAXP; j++) for (int t : fac[i]) f[i][j] = (f[i][j] + f[t][j - 1]) % MOD;
        }

        // 求组合数
        vector<vector<long long>> C;
        C.resize(n + 1, vector<long long>(20));
        C[0][0] = C[1][0] = C[1][1] = 1;
        for (int i = 2; i <= n; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i && j <= MAXP; j++) C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % MOD;
        }

        // 统计最终答案
        long long ans = 0;
        for (int i = 1; i <= K; i++) for (int j = 1; j <= MAXP; j++) ans = (ans + C[n - 1][j - 1] * f[i][j]) % MOD;
        return ans;
    }
};


作者：tsreaper
链接：https://leetcode.cn/problems/count-the-number-of-ideal-arrays/solution/by-tsreaper-bzt9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



const int MOD = 1e9 + 7, MX = 1e4 + 1, MX_K = 13; // 至多 13 个质因数

vector<int> ks[MX]; // ks[x] 为 x 分解质因数后，每个质因数的个数列表

int c[MX + MX_K][MX_K + 1]; // 组合数



int init = []() {

    for (int i = 2; i < MX; ++i) {

        int x = i;

        for (int p = 2; p * p <= x; ++p) {

            if (x % p == 0) {

                int k = 1;

                for (x /= p; x % p == 0; x /= p) ++k;

                ks[i].push_back(k);

            }

        }

        if (x > 1) ks[i].push_back(1);

    }



    c[0][0] = 1;

    for (int i = 1; i < MX + MX_K; ++i) {

        c[i][0] = 1;

        for (int j = 1; j <= min(i, MX_K); ++j)

            c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD;

    }

    return 0;

}();



class Solution {

public:

    int idealArrays(int n, int maxValue) {

        long ans = 0L;

        for (int x = 1; x <= maxValue; ++x) {

            long mul = 1L;

            for (int k: ks[x]) mul = mul * c[n + k - 1][k] % MOD;

            ans += mul;

        }

        return ans % MOD;

    }

};

作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-the-number-of-ideal-arrays/solutions/1659088/shu-lun-zu-he-shu-xue-zuo-fa-by-endlessc-iouh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution {
public:
    int a[200001],b[200001],tmp[200001],h[200001];
    int n,mod;
    void dfs(int *f, int *g) {
        for(int i=1;i<=n;i++) tmp[i]=0;
        for(int i=1;i<=n;i++)
            for(int j=i;j<=n;j+=i) 
                tmp[j]=(tmp[j]+1LL*f[i]*g[j/i]%mod)%mod;
        for(int i=1;i<=n;i++)f[i]=tmp[i];
    }
    void ksm(int k){
        while(k) {
            if (k&1) dfs(a,b);
            k>>=1;
            dfs(b,b);
        }
    }
    int idealArrays(int N, int maxValue) {
        mod=(int)1e9+7;
        h[1]=1;
        n = maxValue;
        for(int i=1;i<=n;i++) a[i]=b[i]=1,h[i]=0;
        ksm(N-1);
        int sum=0;
        for(int i=1;i<=n;i++) sum=(sum+a[i])%mod;
        return sum;
    }
};


// TLE
// using ll = long long;
// class Solution {
// public:
//     int idealArrays(int n, int maxValue) {
//         ll MOD = 1e9+7;
//         vector<ll> dp(maxValue,1);
//         for (int p = 1; p < n; p++){
//             vector<ll> ndp(maxValue,0);
//             for (int v = 1; v*v <= maxValue; v++){
                
//                 ndp[v*v-1] += dp[v-1];
//                 ndp[v*v-1] %= MOD;
//                 for (int i = v+1; v*i <= maxValue; i++){
//                     ndp[v*i-1] += dp[v-1]+dp[i-1];
//                     ndp[v*i-1] %= MOD;
//                 }
//             }
//             swap(dp, ndp);
//         }
//         ll res = 0;
//         for (int i = 0; i < maxValue; i++){
//             res += dp[i];
//             res %= MOD;
//         }
//         return (int)res;
//     }
// };
