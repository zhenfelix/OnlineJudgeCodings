
// #include <bits/stdc++.h>
// #include <vector>
// #include <set>
// #include <map>
#include <algorithm>
// #include <climits>
// #include <iostream>
// #include <unordered_map>
// #include <cstring>
// #include <queue>
#include<cstdio>

#define DEBUG 0

using namespace std;
// using ll = long long;
// using pii = pair<int, int>;
// using pll = pair<ll, ll>;
// using pli = pair<ll, int>;
// using tiii = tuple<int,int,int>;
// using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 1005+50;
const int maxch = 26;
const int maxm = 300000+5;

int t, n, m, x, y, a, b, k;
// ll MOD = (ll)1e9 + 7, h, w;
// int dp[maxn][2],tree[maxn][2],arr[maxm];
// int tot = maxn;
// unordered_map<ll,int> cnt_left, cnt_right;
int arr[maxn], dp[maxn][maxn];

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
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    for (int i = 0; i < n-1; i++) dp[i][i+1] = 0;
    for (int sz = 1; sz <= n-2; sz++){
        for (int i = 0; i+sz+1 < n; i++){
            dp[i][i+sz+1] = 0x3f3f3f3f;
            for (int j = i+1; j <= i+sz; j++){
                dp[i][i+sz+1] = min(dp[i][i+sz+1], dp[i][j]+dp[j][i+sz+1]+arr[i]*arr[j]*arr[i+sz+1]);
            }
        }
    }
    printf("%d\n", dp[0][n-1]);
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
