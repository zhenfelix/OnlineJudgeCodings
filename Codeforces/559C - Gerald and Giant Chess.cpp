
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

#define DEBUG 0

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using tiii = tuple<int,int,int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005+50;
const int maxch = 26;
const int maxm = 2005;

int t, n, m, x, y;
ll MOD = (ll)1e9 + 7, h, w;
pll pos[maxm];
ll fac[maxn], ifac[maxn], cb[maxm][maxm], dp[maxm][maxm];

std::ostream &operator<<(std::ostream &stream,
                         vector<pii> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}

std::ostream &operator<<(std::ostream &stream,
                         vector<int> &v)
{
    for (auto x : v)
        stream << x << "-";
    return stream;
}

std::ostream &operator<<(std::ostream &stream,
                         vector<ll> &v)
{
    for (auto x : v)
        stream << x << "-";
    return stream;
}

template<class T>
void debug_arr(T a[], int start, int end){
    if (!DEBUG) return;
    for (int i = start; i <= end; i++) cout << a[i] << " ";
    cout << endl;
}

void debug_combination(int mx){
    if (!DEBUG)
        return;
    for (int i = 0; i <= mx; i++){
        for (int j = 0; j <= i; j++){
            ll val = (((fac[i] * ifac[j]) % MOD) * ifac[i-j]) % MOD;
            printf("%d %d: %lld; ", i, j, val);
        }
    }
}

bool myless(string a, string b){
    return a.length() < b.length() || (a.length() == b.length() && a < b);
}

ll quickmulti(ll a, ll p){
    ll ans = 1;
    while (p){
        if (p&1) ans = (ans*a)%MOD;
        a = (a*a)%MOD;
        p >>= 1;
    }
    return ans;
}

inline ll calc(ll a, ll b){
    return (((fac[a+b] * ifac[b]) % MOD) * ifac[a]) % MOD;
}

void solve()
{
    scanf("%lld%lld%d", &h, &w, &n);
    for (int i = 0; i < n; i++){
        scanf("%d%d", &x, &y);
        pos[i] = {x,y};
    }
    sort(pos, pos+n);
    pos[n] = {h,w};
    ll mx = h+w;
    fac[0] = 1;
    for (int i = 1; i <= mx; i++) fac[i] = (fac[i-1]*i)%MOD;
    ifac[mx] = quickmulti(fac[mx], MOD-2);
    for (int i = mx-1; i >= 0; i--) ifac[i] = (ifac[i+1]*(i+1))%MOD;
    debug_combination(mx);
    for (int i = 0; i < n; i++){
        auto [ri, ci] = pos[i];
        for (int j = i+1; j <= n; j++){
            auto [rj, cj] = pos[j];
            if (ri <= rj && ci <= cj){
                if (ri == rj || ci == cj) cb[i][j] = 1;
                else{
                    rj -= ri;
                    cj -= ci;
                    cb[i][j] = calc(rj,cj);
                }
                
            }
            else{
                cb[i][j] = 0;
            }
        }
    }
    for (int i = 0; i <= n; i++){
        auto [r,c] = pos[i];
        r--;c--;
        dp[0][i] = calc(r,c);
    }
    for (int i = 1; i <= n; i++){
        for (int j = i; j <= n; j++){
            dp[i][j] = (dp[i-1][j]+MOD-(dp[i-1][i-1]*cb[i-1][j])%MOD)%MOD;
        }
    }
    printf("%lld\n", dp[n][n]);
}



int main()
{
    // freopen("input", "r", stdin);
#ifndef ONLINE_JUDGE
    freopen("input", "r", stdin);
#endif
    solve();
    // scanf("%d\n", &t);
    // while (t--){
        
    // }

}
