#include<bits/stdc++.h> 
using namespace std;
using LL = long long;
const int s = 9;
// n < 2^78
const LL p[9] = {2, 3, 5, 7, 11, 13, 17, 19, 23};
mt19937_64 rnd(random_device{}());

LL mul(LL a, LL b, LL p){
    // return __int128(a) * b % p;
    a %= p, b %= p;
    LL c = (long double)a * b / p;
    LL ans = a * b - c * p;
    if (ans < 0)
        ans += p;
    else if (ans >= p)
        ans -= p;
    return ans;
}

LL qpow(LL a, LL n, LL p){
    LL ans = 1;
    a %= p;
    while (n){
        if (n & 1) ans = mul(ans, a, p);
        a = mul(a, a, p);
        n >>= 1;
    }
    return ans;
}

bool check(LL a, LL n, LL x, LL t){
    LL ret = qpow(a, x, n);
    LL last = ret;
    for (int i = 1; i <= t; i++){
        ret = mul(ret, ret, n);
        if (ret == 1 && last != 1 && last != n - 1)
            return true;
        last = ret;
    }
    if (ret != 1) return true;
    else return false;
}

bool Miller_Rabin(LL n){
    if (n < 2) return false;
    for(auto x : p) if (n == x) return true;
    if ((n & 1) == 0) return false;

    LL x = n - 1;
    LL t = 0;
    while ((x & 1) == 0){
        x >>= 1;
        t++;
    }

    for (int i = 0; i < s; i++){
        // LL a = uniform_int_distribution<LL>(1, n - 1)(rnd);
        // if (check(a, n, x, t))
        if (check(p[i], n, x, t)) return false;
    }
    return true;
}


LL Pollard_rho(LL x){
    LL s = 0, t = 0, c = uniform_int_distribution<LL>(1, x - 1)(rnd);
    LL step = 0, goal = 1;
    LL val = 1;
    for (goal = 1;; goal <<= 1, s = t, val = 1){
        for (step = 1; step <= goal; ++step){
            t = (mul(t, t, x) + c) % x;
            val = mul(val, abs(t - s), x);
            if ((step % 127) == 0){
                LL d = __gcd(val, x);
                if (d > 1)
                    return d;
            }
        }
        LL d = __gcd(val, x);
        if (d > 1) return d;
    }
}
LL fac[200], tot;

void findfac(LL n){
    if (n == 1) return;
    if (Miller_Rabin(n)){
        fac[++tot] = n;
        return;
    }
    LL p = n;
    while (p >= n) p = Pollard_rho(n);
    while (n % p == 0) n /= p;
    findfac(n);
    findfac(p);
}

// void go_fac(LL n){ 
//     tot = 0;
//     if (n > 1) findfac(n); 
// }

//void dfs(int u, LL val, const vector<pair<LL, int> > &pri, vector<LL> &f){
//    if (u == pri.size()){
//        f.push_back(val);
//        return;
//    }
//    int c = pri[u].second;
//    for(int i = 0; i <= c; i++){
//        dfs(u + 1, val, pri, f);
//        val *= pri[u].first;
//    }
//}

LL go_fac(LL n){ 
   tot = 0;
   if (n > 1) findfac(n);     
   map<LL, int> mp;
   vector<pair<LL, int> > pri;
   LL ans = 0;
   for(int i = 1; i <= tot; i++){
       if (mp.count(fac[i])) continue;
       int c = 0;
       while(n % fac[i] == 0) c += 1, n /= fac[i];
       mp[fac[i]] = c;
       ans += c * fac[i];
   }
   return ans;
}

int main(){

#ifdef LOCAL
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
#endif

    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);

    int n, a, b;
    cin >> n >> a >> b;
    vector<int> x(n + 1), f(n + 1);
    vector<vector<pair<int, int> > > g(2 * n + 1);
    for(int i = 1; i <= n; i++){
        cin >> x[i];
        f[i] = go_fac(x[i]) % n + 1;
        g[i].push_back({n + f[i], 0});
        g[n + f[i]].push_back({i, 1});
    }
    for(int i = 1; i <= n; i++){
        g[n + f[i]].push_back({f[i], 1});
        g[f[i]].push_back({n + f[i], 0});
    }
    const int INF = 1e9;
    vector<int> d(2 * n + 1, INF);
    d[a] = 0;
    deque<int> q;
    vector<bool> v(2 * n + 1);

    q.push_back(a);
    while(!q.empty()){
        int t = q.front();
        q.pop_front();
        if (v[t]) continue;
        v[t] = true;
        for(auto [j, w] : g[t]){
            if (d[t] + w < d[j]){
                d[j] = d[t] + w;
                if (w == 0){
                    q.push_front(j);
                }
                else{
                    q.push_back(j);
                }
            }
        }
    }
    if (d[b] > INF / 2) cout << -1 << '\n';
    else cout << d[b] << '\n';

}













#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<set>
#include<algorithm>
#include<map>
#include<iostream>
#include<cmath>
using namespace std;

bool ispri(int x) {
    for (int i=2;1ll*i*i<=x;i++) {
        if (x%i == 0) return false;
    }
    return true;
}

vector<int> get_pri() {
    vector<int> pri;
    for (int i=2;i<=1e4+1;i++) {
        if (ispri(i)) {
            pri.push_back(i);
        }
    }
    return pri;
}

int n, a[200005], f[200005];

int maxp;
vector<int> e[400005];

void edge(int u, int v) {
    e[u].push_back(v);
}
void edge2(int u, int v) {
    edge(u, v);
    edge(v, u);
}

int que[400005];
int vis[400005];
int dis[400005];

int work(int s, int t) {
    int l=1, r=1;

    que[1] = s;
    vis[s] = 1;

    for(int i=1;i<=maxp;i++) dis[i] = -2;
    dis[s] = 0;

    while (l<=r) {
        int pos = que[l++];
        for (int y: e[pos]) {
            if (vis[y]) continue;
            vis[y] = 1;
            dis[y] = dis[pos] + 1;
            que[++r] = y;
        }
    }
    
    return dis[t];

}
int bfs(int u, int v) {
    // int ret = work(u, v);
    // if (ret > 1e8) return -1;
    // return ret;
    return work(u, v);
}
int main()
{
    int A, B;
    vector<int> pri = get_pri();
    scanf("%d%d%d", &n, &A, &B);
    for (int i=1;i<=n;i++) scanf("%d", &a[i]);
    maxp = 2*n;
    for (int i=1;i<=n;i++) {
        int val = a[i];
        int sum = 0;
        for (auto p : pri) {
            while (val%p == 0) {
                sum += p;
                val/=p;
            }
        }
        if (val != 1) sum += val;

        int fval = sum%n+1;
        edge2(i, fval+n);
        maxp++;
        edge2(i, maxp);
        edge2(maxp, fval);

    }
    printf("%d\n", bfs(A, B)/2);
    return 0;
}