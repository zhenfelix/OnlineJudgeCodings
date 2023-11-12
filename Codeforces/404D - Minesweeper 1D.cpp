
// #include <bits/stdc++.h>

// using namespace std;
// using ll = long long;
// ll MOD = 998244353;

// void solve() {
//     int n,m,a,k,l,r;
//     cin >> n >> m;
//     vector<int> col(n), row(m), pre(m,0);
//     for (int i = 0; i < n; i++) {
//         col[i] = n;
//         for (int j = 0; j < m; j++) {
//             cin >> a;
//             if (a < pre[j]) row[j] = i;
//             pre[j] = a;
//             col[i] = min(col[i],row[j]);
//         }
//     }
//     cin >> k;
//     for (int i = 0; i < k; i++) {
//         cin >> l >> r;
//         if (l-1 < col[r-1]) cout << "No";
//         else cout << "Yes";
//         cout << endl;
//     }
// }

// int main(){
//     ios_base::sync_with_stdio(0);
//     cin.tie(0);
// #ifndef ONLINE_JUDGE 
//     freopen("input","r",stdin);
// #endif
//     int t = 1;
//     // cin >> t;
//     while (t--) solve();
//     return 0;
// }


#include <iostream>
#include <cmath>
#include<cstring>

using namespace std;
using ll = long long;

const ll MOD = 1e9+7;
const int nmax = 1e6+10;

ll dp[nmax][2][2];

ll dfs(int i, int cur, int nxt, string &s) {
    if (i < 0) return cur == 0 ? 1 : 0;
    if (dp[i][cur][nxt] != -1) return dp[i][cur][nxt];
    ll ans = 0;
    char ch = s[i];
    if (ch == '*' || ch == '?'){
        if (cur == 1 || ch == '?') {
            ans += dfs(i-1,0,cur,s);
            ans += dfs(i-1,1,cur,s);
        }
    }
    else if (cur != 1) {
        for (int pre = 0; pre < 2; pre++) {
            if (ch-'0' == pre+nxt) ans += dfs(i-1,pre,cur,s);
        }
    }
    ans %= MOD;
    dp[i][cur][nxt] = ans;
    return ans;
}

void solve() {
    string s;
    cin >> s;
    int n = s.length();
    for(int i = 0; i < n; i++)for(int cur = 0; cur < 2; cur++)for(int nxt = 0; nxt < 2; nxt++) dp[i][cur][nxt] = -1;
    ll res = (dfs(n-1,0,0,s)+dfs(n-1,1,0,s))%MOD;
    cout << res << endl;
    return;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
#ifndef ONLINE_JUDGE 
    freopen("input","r",stdin);
#endif
    // int t;
    // cin >> t;

    // for (int i = 0; i < t; ++i) {
    //     solve();
    // }
    solve();
    return 0;
}
