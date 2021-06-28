// class Solution {
// private:
//     static constexpr int mod = 1000000007;
//     using LL = long long;

// public:
//     int waysToBuildRooms(vector<int>& prevRoom) {
        
//         // 快速幂计算 x^y
//         auto quickmul = [&](int x, int y) {
//             int ret = 1, cur = x;
//             while (y) {
//                 if (y & 1) {
//                     ret = (LL)ret * cur % mod;
//                 }
//                 cur = (LL)cur * cur % mod;
//                 y >>= 1;
//             }
//             return ret;
//         };
        
//         int n = prevRoom.size();
//         // fac[i] 表示 i!
//         // inv[i] 表示 i! 的乘法逆元
//         vector<int> fac(n), inv(n);
//         fac[0] = inv[0] = 1;
//         for (int i = 1; i < n; ++i) {
//             fac[i] = (LL)fac[i - 1] * i % mod;
//             // 使用费马小定理计算乘法逆元
//             inv[i] = quickmul(fac[i], mod - 2);
//         }
        
//         // 构造树
//         vector<vector<int>> edges(n);
//         for (int i = 1; i < n; ++i) {
//             edges[prevRoom[i]].push_back(i);
//         }
        
//         vector<int> f(n), cnt(n);
//         function<void(int)> dfs = [&](int u) {
//             f[u] = 1;
//             for (int v: edges[u]) {
//                 dfs(v);
//                 // 乘以左侧的 f[ch] 以及右侧分母中 cnt[ch] 的乘法逆元
//                 f[u] = (LL)f[u] * f[v] % mod * inv[cnt[v]] % mod;
//                 cnt[u] += cnt[v];
//             }
//             // 乘以右侧分子中的 (cnt[i] - 1)!
//             f[u] = (LL)f[u] * fac[cnt[u]] % mod;
//             ++cnt[u];
//         };
        
//         dfs(0);
//         return f[0];
//     }
// };


// // 作者：LeetCode-Solution
// // 链接：https://leetcode-cn.com/problems/count-ways-to-build-rooms-in-an-ant-colony/solution/tong-ji-wei-yi-qun-gou-zhu-fang-jian-de-uqhn7/
// // 来源：力扣（LeetCode）
// // 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


using ll = long long;
const ll MOD = 1e9 + 7;
const int N = 100005;

bool inited = false;
ll fac[N], ifac[N], ans[N];
int sz[N];
vector<vector<int>> adj;
ll fexp(ll x, ll y) {
    ll ans = 1;
    while (y) {
        if (y & 1)
            ans = ans * x % MOD;
        x = x * x % MOD;
        y >>= 1;
    }
    return ans;
}
ll C(int n, int k) {
    return fac[n] * ifac[k] % MOD * ifac[n - k] % MOD;
}

void init() {
    inited = true;
    fac[0] = ifac[0] = 1;
    for (int i = 1; i < N; ++i)
        fac[i] = fac[i - 1] * i % MOD;
    ifac[N - 1] = fexp(fac[N - 1], MOD - 2);
    for (int i = N - 2; i >= 1; --i)
        ifac[i] = ifac[i + 1] * (i + 1) % MOD;
}

void dfs(int u) {
    sz[u] = 0;
    for (int v : adj[u]) {
        dfs(v);
        sz[u] += sz[v];
    }
    
    int tot = sz[u];
    ans[u] = 1;
    for (int v : adj[u]) {
        ans[u] = ans[u] * ans[v] % MOD;
        ans[u] = ans[u] * C(tot, sz[v]) % MOD;
        tot -= sz[v];
    }
    
    sz[u]++;
}

class Solution {
public:
    int waysToBuildRooms(vector<int>& prevRoom) {
        if (!inited)
            init();
        
        int n = prevRoom.size();
        adj = vector<vector<int>>(n);
        for (int i = 1; i < n; ++i)
            adj[prevRoom[i]].emplace_back(i);
        
        dfs(0);
        
        return ans[0];
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/6LY3tn/view/TG6U7W/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。