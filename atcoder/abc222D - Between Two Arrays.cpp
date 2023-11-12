
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
ll MOD = 998244353;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
#ifndef ONLINE_JUDGE 
    freopen("input","r",stdin);
#endif
    int n;
    const int nmax = 3005;
    cin >> n;
    vector<ll> arr(n), brr(n), dp(nmax,1);
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n; i++) cin >> brr[i];
    for (int i = 0; i < n; i++) {
        int lo = arr[i], hi = brr[i];
        for (int j = 0; j < nmax; j++) if (j < lo || j > hi) dp[j] = 0;
        for (int j = 1; j < nmax; j++) dp[j] = (dp[j]+dp[j-1])%MOD;
    }
    cout << dp.back() << endl;
    return 0;
}