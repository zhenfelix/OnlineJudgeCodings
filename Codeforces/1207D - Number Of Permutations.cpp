
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
const int maxn = 300005+50;
const int maxch = 26;
const int maxm = 300000+5;

const int MOD = 998244353;

int t, n, m, x, y, a, b, k;
// ll MOD = (ll)1e9 + 7, h, w;
// int dp[maxn][2],tree[maxn][2],arr[maxm];
// int tot = maxn;
// unordered_map<ll,int> cnt_left, cnt_right;
// int arr[maxn], dp[maxn][maxn];
int cnta[maxn], cntb[maxn];
ll f[maxn];

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
void solve()
{
    scanf("%d",&n);
    f[0] = 1;
    for (int i = 1; i <= n; i++) f[i] = (f[i-1]*i)%MOD;
    memset(cnta, 0, (n+1)*sizeof(int));
    memset(cntb, 0, (n+1)*sizeof(int));
    
    
    vector<pii> arr;
    for (int i = 1; i <= n; i++) {
        cin >> a >> b;
        arr.push_back({a,b});
        cnta[a]++;cntb[b]++;
    }
    sort(arr.begin(), arr.end());
    ll cntab = 1, cc = 1;
    bool flag = true;
    for (int i = 1; i < n; i++){
        if (arr[i].second < arr[i-1].second){
            flag = false;
            break;
        }
        if ((arr[i].second == arr[i - 1].second)&&(arr[i].first == arr[i-1].first)){
            cc++;
        }
        else{
            cntab = (f[cc]*cntab)%MOD;
            cc = 1;
        }
    }
    cntab = (f[cc]*cntab)%MOD;
    ll res = 0, ca = 1, cb = 1;
    for (int i = 1; i <= n; i++){
        ca = (ca*f[cnta[i]])%MOD;
        cb = (cb*f[cntb[i]])%MOD; 
    }
    res = (res+ca)%MOD;
    res = (res+cb)%MOD;
    if (flag) res = (res+MOD-cntab)%MOD;
    res = (f[n]+MOD-res)%MOD;
    printf("%lld\n", res);
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
