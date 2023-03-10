
#include <bits/stdc++.h>
// #include <vector>
// #include <set>
// #include <map>
// #include <algorithm>
// #include <climits>
// #include <iostream>
// #include <unordered_map>
// #include <cstring>
// #include <queue>
// #include<cstdio>

#define DEBUG 0

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using pli = pair<ll, int>;
using tiii = tuple<int,int,int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 3000 + 5;
const int maxch = 26;
const int maxm = 3000+5;

const int MOD = 998244353;

int t, n, m, x, y, a, b, k;
// ll MOD = (ll)1e9 + 7, h, w;
// int dp[maxn][2],tree[maxn][2],arr[maxm];
// int tot = maxn;
// unordered_map<ll,int> cnt_left, cnt_right;
// int arr[maxn], dp[maxn][maxn];
// int cnt[maxn][maxn], arr[maxn];
// ll f[maxn];

// std::ostream &operator<<(std::ostream &stream,
//                          vector<pii> &v)
// {
//     for (auto [ch,i] : v) stream << ch << ": " << i << " ";
//     return stream;
// }

// std::ostream &operator<<(std::ostream &stream,
//                          vector<int> &v)
// {
//     for (auto x : v)
//         stream << x << "-";
//     return stream;
// }

// std::ostream &operator<<(std::ostream &stream,
//                          vector<ll> &v)
// {
//     for (auto x : v)
//         stream << x << "-";
//     return stream;
// }

// template<class T>
// void debug_arr(T a[], int start, int end){
//     if (!DEBUG) return;
//     for (int i = start; i <= end; i++) cout << a[i] << " ";
//     cout << endl;
// }

// // void debug_combination(int mx){
// //     if (!DEBUG)
// //         return;
// //     for (int i = 0; i <= mx; i++){
// //         for (int j = 0; j <= i; j++){
// //             ll val = (((fac[i] * ifac[j]) % MOD) * ifac[i-j]) % MOD;
// //             printf("%d %d: %lld; ", i, j, val);
// //         }
// //     }
// // }

// bool myless(string a, string b){
//     return a.length() < b.length() || (a.length() == b.length() && a < b);
// }

// ll quickmulti(ll a, ll p){
//     ll ans = 1;
//     while (p){
//         if (p&1) ans = (ans*a)%MOD;
//         a = (a*a)%MOD;
//         p >>= 1;
//     }
//     return ans;
// }

// void clear(){
//     // for (int i = 0; i < tot; i++){
//     //     for (int j = 0; j < 2; j++){
//     //         dp[i][j] = 0;
//     //         tree[i][j] = -1;
//     //     }
//     // }
//     memset(dp, 0, tot*2*sizeof(int));
//     memset(tree, -1, tot * 2 * sizeof(int));
// }

// void dfs(int cur, int parent, ll& u, ll& v, vector<vector<int>> &g, vector<int> &arr){
//     for (auto nxt : g[cur]){
//         if (nxt == parent) continue;
//         ll nu = 0, nv = 0;
//         dfs(nxt, cur, nu, nv, g, arr);
//         u = max(u, nu);
//         v = max(v, nv);
//     }
//     int a = arr[cur];
//     if (u+a >= v) v = u+a;
//     else u = v-a;
// }

void solve()
{
    int n, m, d;
    scanf("%d%d%d",&n, &m, &d);
    vector<vector<int>> g(n);
    vector<bool> monster(n, false);
    vector<int> dist(n,-n), ndist(n,-n-n);
    for (int i = 0; i < m; i++){
        int tmp;
        scanf("%d", &tmp);
        monster[tmp-1] = true;
    }
    for (int i = 0; i < n-1; i++){
        int a, b;
        scanf("%d%d", &a, &b);
        g[a-1].push_back(b-1);
        g[b-1].push_back(a-1);
    }
    function<void(int,int)> dfs = [&] (int cur, int parent){
        if (monster[cur]) dist[cur] = 0;
        for (auto nxt : g[cur]){
            if (parent == nxt) continue;
            dfs(nxt,cur);
            if (dist[nxt]+1 > dist[cur]){
                ndist[cur] = dist[cur];
                dist[cur] = dist[nxt]+1;
            }
            else if (dist[nxt]+1 > ndist[cur]){
                ndist[cur] = dist[nxt]+1;
            }
        }
        return;
    };
    dfs(0,0);
    int ans = 0;
    function<void(int,int,int)> dfs2 = [&] (int cur, int parent, int up){
        // printf("%d %d\n", cur, up);
        if (max(dist[cur],up) <= d) ans++;
        for (auto nxt: g[cur]){
            if (nxt == parent) continue;
            if (dist[nxt]+1 == dist[cur]){
                dfs2(nxt, cur, max(up,ndist[cur])+1);
            }
            else{
                dfs2(nxt, cur, max(up,dist[cur])+1);
            }
        }
    };
    dfs2(0,0,-n-n);
    printf("%d\n",ans);
    
    
    return;
}



int main()
{
#ifndef ONLINE_JUDGE
    freopen("contests/input", "r", stdin);
#endif
    // scanf("%d", &t);
    t = 1;
    while (t--)
    {
        solve();
    }

}
