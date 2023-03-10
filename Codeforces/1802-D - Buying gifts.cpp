
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
    int n, a, b;
    // scanf("%d%d%d",&n, &m, &d);
    scanf("%d\n", &n);
    vector<pii> arr(n);
    for (int i = 0; i < n; i++){
        scanf("%d%d\n", &a, &b);
        arr[i] = {a,b};
    }
    sort(arr.begin(), arr.end(), [&](pii x, pii y){
        if (x.first < y.first || (x.first == y.first && x.second > y.second)) return true;
        return false;
    });
    map<int,int> mp;
    for (int i = 0; i < n; i++)mp[arr[i].second]++;
    ll inf = 2e9;
    ll mx = -inf, ans = inf;
    for (int i = n-1; i >= 0; i--){
        auto &[a,b] = arr[i];
        mp[b]--;
        if (mp[b] == 0) mp.erase(b);
        auto it = mp.upper_bound(a);
        ll l = -inf, r = inf;
        if (!mp.empty()){
            if (it == mp.end())
                r = inf;
            else
                r = it->first;
            if (it == mp.begin())
                l = -inf;
            else
            {
                it--;
                l = it->first;
            }
        }
        ans = min(ans, abs(mx-a));
        if (r > mx) ans = min(ans, abs(r-a));
        if (l > mx) ans = min(ans, abs(l-a));
        if (mx > a) break;
        mx = max(mx, (ll)b);
    }
    printf("%lld\n", ans);
    
    return;
}



int main()
{
#ifndef ONLINE_JUDGE
    freopen("contests/input", "r", stdin);
#endif
    scanf("%d", &t);
    // t = 1;
    while (t--)
    {
        solve();
    }

}
