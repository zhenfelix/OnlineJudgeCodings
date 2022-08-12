
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
const int maxn = 2e5+50;
const int maxch = 26;

int t, n, m, x, y, k;
ll MOD = 998244353, h, w;
ll dp[maxn], ans[maxn];


void solve()
{
    scanf("%d%d", &n, &k);
    memset(dp, 0, sizeof(dp));
    memset(ans, 0, sizeof(ans));
    ll sums = 0;
    dp[0] = 1;
    for (int i = 0; sums+i+k <= n; i++){
        sums += i + k;
        for (int j = 1; j <= n; j++){
            if (j >= i+k) dp[j] = (dp[j-i-k]+dp[j])%MOD;
        }
        for (int j = sums; j <= n; j++){
            ans[j] = (ans[j]+dp[j-sums])%MOD;
        }
        
    }
    for (int j = 1; j <= n; j++){
        printf("%lld\n", ans[j]);
    }
    return;
}



int main()
{
#ifndef ONLINE_JUDGE
    freopen("contests/input", "r", stdin);
#endif
    t = 1;
    while (t--)
    {
        solve();
    }
    

}
