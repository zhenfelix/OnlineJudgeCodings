#include<bits/stdc++.h>

using namespace std;
using ll = long long;

using pii = pair<int,int>;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input", "r", stdin);
    int t;
    cin >> t;
    while (t--)
    {
        int n,k,p;
        cin >> n >> k;
        unordered_map<int,int> mp;
        vector<int> score(n), child(n,0);
        vector<ll> mx(n);
        vector<vector<int>> g(n);
        for (int i = 1; i < n; i++) {
            cin >> p;
            g[p-1].push_back(i);
            child[p-1]++;
        }
        for (int i = 0; i < n; i++){
            cin >> score[i];
            mx[i] = score[i];
        }
        ll ans = 0;
        function<void(int,int)> dfs = [&] (int cur, int pcnt) {
            ans += (ll)score[cur]*pcnt;
            if (child[cur] == 0) return;
            int r = pcnt%child[cur];
            int np = pcnt/child[cur];
            for (auto nxt : g[cur]){
                dfs(nxt, np);
            }
            sort(g[cur].begin(), g[cur].end(), [&](int x, int y) {
                return mx[x] > mx[y];
            });
            for (int i = 0; i < r; i++){
                ans += (ll)mx[g[cur][i]];
            }
            mx[cur] += mx[g[cur][r]];
            
        };
        dfs(0,k);
        cout << ans << endl;
    }
    
    return 0;
}





cuiaoxiang
// #define LOCAL
#define _USE_MATH_DEFINES
#include <array>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <complex>
#include <cmath>
#include <numeric>
#include <bitset>
#include <functional>
#include <random>
#include <ctime>

using namespace std;

template <typename A, typename B>
ostream& operator <<(ostream& out, const pair<A, B>& a) {
  out << "(" << a.first << "," << a.second << ")";
  return out;
}
template <typename T, size_t N>
ostream& operator <<(ostream& out, const array<T, N>& a) {
  out << "["; bool first = true;
  for (auto& v : a) { out << (first ? "" : ", "); out << v; first = 0;} out << "]";
  return out;
}
template <typename T>
ostream& operator <<(ostream& out, const vector<T>& a) {
  out << "["; bool first = true;
  for (auto v : a) { out << (first ? "" : ", "); out << v; first = 0;} out << "]";
  return out;
}
template <typename T, class Cmp>
ostream& operator <<(ostream& out, const set<T, Cmp>& a) {
  out << "{"; bool first = true;
  for (auto& v : a) { out << (first ? "" : ", "); out << v; first = 0;} out << "}";
  return out;
}
template <typename T, class Cmp>
ostream& operator <<(ostream& out, const multiset<T, Cmp>& a) {
  out << "{"; bool first = true;
  for (auto& v : a) { out << (first ? "" : ", "); out << v; first = 0;} out << "}";
  return out;
}
template <typename U, typename T, class Cmp>
ostream& operator <<(ostream& out, const map<U, T, Cmp>& a) {
  out << "{"; bool first = true;
  for (auto& p : a) { out << (first ? "" : ", "); out << p.first << ":" << p.second; first = 0;} out << "}";
  return out;
}
#ifdef LOCAL
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
#else
#define trace(...) 42
#endif
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
  cerr << name << ": " << arg1 << endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
  const char* comma = strchr(names + 1, ',');
  cerr.write(names, comma - names) << ": " << arg1 << " |";
  __f(comma + 1, args...);
}

template <class T> auto vect(const T& v, int n) { return vector<T>(n, v); }
template <class T, class... D> auto vect(const T& v, int n, D... m) {
  return vector<decltype(vect(v, m...))>(n, vect(v, m...));
}

using int64 = long long;
using int128 = __int128_t;
using ii = pair<int, int>;
#define SZ(x) (int)((x).size())
template <typename T> static constexpr T inf = numeric_limits<T>::max() / 2;
const int MOD = 1e9 + 7;
// const int MOD = 998244353;
mt19937_64 mrand(random_device{}());
int64 rnd(int64 x) { return mrand() % x; }
constexpr inline int lg2(int64 x) { return sizeof(int64) * 8 - 1 - __builtin_clzll(x); }
template <class T> void out(const vector<T>& a) { for (int i = 0; i < SZ(a); ++i) cout << a[i] << " \n"[i + 1 == SZ(a)]; }
template <class T> bool ckmin(T& a, const T& b) { return b < a ? a = b, 1 : 0; }
template <class T> bool ckmax(T& a, const T& b) { return a < b ? a = b, 1 : 0; }
template <class T> void dedup(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()), v.end()); }
inline void add_mod(int& x, int y) { x += y; if (x >= MOD) x -= MOD; }
inline void sub_mod(int& x, int y) { x += MOD - y; if (x >= MOD) x -= MOD; }
inline int mod(int x) { return x >= MOD ? x - MOD : x; }

struct fast_ios {
  fast_ios() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    cout << fixed << setprecision(10);
  };
} fast_ios_;

int main() {
  int cas;
  cin >> cas;
  while (cas--) {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> a(n);
    for (int i = 1; i < n; ++i) {
      int p;
      cin >> p;
      --p;
      a[p].push_back(i);
    }
    vector<int64> s(n);
    for (int i = 0; i < n; ++i) cin >> s[i];

    // vector<int64> best(n);
    // function<void(int)> dfs =
    //   [&](int u) {
    //     best[u] = 0;
    //     for (auto& v : a[u]) {
    //       dfs(v);
    //       ckmax(best[u], best[v]);
    //     }
    //     best[u] += s[u];
    //     trace(u, a[u], best[u]);
    //   };
    // dfs(0);
    // trace(best);
    int64 ret = 0;
    function<int64(int, int)> solve =
      [&](int u, int cnt) {
        int m = SZ(a[u]);
        ret += cnt * s[u];
        if (m == 0) return s[u];
        int q = cnt / m, r = cnt % m;
        trace(u, a[u], cnt, q, r, ret);
        vector<pair<int64, int>> can;
        for (auto& v : a[u]) {
          int64 cur = solve(v, q);
          can.push_back({cur, v});
        }
        sort(can.rbegin(), can.rend());
        trace(u, can);
        for (int i = 0; i < r; ++i) ret += can[i].first;
        trace(u, cnt, m, q, r, can[r].first, s[u]);
        return can[r].first + s[u];
      };
    solve(0, m);
    cout << ret << '\n';
  }

  return 0;
}












/**
 * Created by megurine on 2022/10/15 23:13:21.
 * 诸天神佛，佑我上分！
 **/
#include <bits/stdc++.h>

using namespace std;

#define fastIO() ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr)
#define itr(it) begin(it), end(it)
typedef long long ll;
typedef pair<int, int> PII;
typedef double db;
typedef long double ld;
typedef unsigned long long ull;
#define endl '\n'
#define YES() cout << "YES\n"
#define NO() cout << "NO\n"

template<typename T>
void chmax(T &a, T b) { if (b > a) a = b; }

template<typename T>
void chmin(T &a, T b) { if (b < a) a = b; }

void solve() {
    int n, k;
    cin >> n >> k;
    vector<vector<int>> g(n);
    for (int i = 1; i < n; ++i) {
        int p;
        cin >> p;
        g[p - 1].emplace_back(i);
    }
    vector<int> val(n);
    for (auto &x: val) cin >> x;
    map<PII, ll> mp;
    function<ll(int, int)> dfs = [&](int u, int k) -> ll {
        if (k == 0) return 0;
        ll ret = ll(k) * val[u];
        if (g[u].empty()) return ret;
        if (mp.count(PII{u, k})) return mp[PII{u, k}];
        if (k % g[u].size() == 0) {
            for (auto v: g[u]) {
                ret += dfs(v, k / g[u].size());
            }
            return ret;
        } else {
            int kk = k / g[u].size(), cc = k % g[u].size();
            vector<pair<ll, ll>> pp;
            for (auto v: g[u]) {
                pp.emplace_back(dfs(v, kk + 1), dfs(v, kk));
            }
            std::sort(pp.begin(), pp.end(), [](auto &a, auto&b) -> bool {
                return a.first - a.second > b.first - b.second;
            });
            for (int i = 0; i < g[u].size(); ++i) {
                if (i >= cc) {
                    ret += pp[i].second;
                } else {
                    ret += pp[i].first;
                }
            }
        }
        return mp[PII{u, k}] = ret;
    };
    ll ans = dfs(0, k);
    cout << ans << endl;
}

int main() {
#ifdef MEGURINE
#define fr(x) freopen(x, "r", stdin)
#define fw(x) freopen(x, "w", stdout)
    fr("../input.txt");
    fw("../output.txt");
    clock_t start = clock();
#endif
    fastIO();
    int T = 1;
    cin >> T;
    cout << fixed << setprecision(12);
    while (T--) {
        solve();
    }
    cout.flush();
#ifdef MEGURINE
    clock_t end = clock();
    cout << "\n\nRunning Time : " << (double) (end - start) / CLOCKS_PER_SEC * 1000 << "ms" << endl;
#endif
    return 0;
}









jiangly
#include <bits/stdc++.h>

using i64 = long long;

void solve() {
    int n, k;
    std::cin >> n >> k;
    
    std::vector<int> p(n), d(n);
    for (int i = 1; i < n; i++) {
        std::cin >> p[i];
        p[i]--;
        d[p[i]]++;
    }
    
    std::vector<int> s(n);
    for (int i = 0; i < n; i++) {
        std::cin >> s[i];
    }
    
    std::vector<std::vector<int>> adj(n);
    for (int i = 1; i < n; i++) {
        adj[p[i]].push_back(i);
    }
    
    std::vector<std::array<int, 2>> f(n);
    std::vector<std::array<i64, 2>> dp(n);
    std::function<void(int)> dfs = [&](int x) {
        for (auto y : adj[x]) {
            f[y][0] = f[x][0] / d[x];
            f[y][1] = (f[x][1] + d[x] - 1) / d[x];
            dfs(y);
        }
        std::sort(adj[x].begin(), adj[x].end(), [&](int i, int j) {
            return dp[i][1] - dp[i][0] > dp[j][1] - dp[j][0];
        });
        for (auto k : {0, 1}) {
            int t = f[x][k];
            dp[x][k] = 1LL * s[x] * t;
            for (int j = 0; j < d[x]; j++) {
                dp[x][k] += dp[adj[x][j]][f[adj[x][j]][0] * d[x] + j < t];
            }
        }
    };
    f[0] = {k, k};
    dfs(0);
    
    std::cout << dp[0][0] << "\n";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    int t;
    std::cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}