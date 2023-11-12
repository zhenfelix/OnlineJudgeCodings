#include<bits/stdc++.h>

using namespace std;
using ll = long long;
int main() {
    #ifndef ONLINE_JUDGE
    freopen("input","r",stdin);
    #endif
    string s;
    cin >> s;
    ll x;
    cin >> x;
    vector<int> target, source;
    while (x > 0 || !s.empty()) {
        target.push_back(x&1);
        x >>= 1;
        if (!s.empty()) {
            if (s.back() != '?') source.push_back(s.back()-'0');
            else source.push_back(-1);
            s.pop_back();
        }
        else source.push_back(0);
    }
    int n = target.size();
    vector<vector<ll>> dp(n+1,vector<ll>(2,-1));
    dp[0][0] = dp[0][1] = 0;
    ll base = 1;
    for (int i = 0; i < n; i++) {
        for (int f = 0; f < 2; f++) {
            for (int g = 0; g < 2; g++) {
                if (source[i] >= 0) {
                    if (g != source[i]) continue;
                }
                if (f == 0) {
                    if (dp[i][0] >= 0) dp[i+1][0] = max(dp[i+1][0],dp[i][0]+base*g);
                }
                else {
                    if (g == target[i]) {
                        if (dp[i][1] >= 0) dp[i+1][1] = max(dp[i+1][1],dp[i][1]+base*g);
                    }
                    else if (g < target[i]){
                        if (dp[i][0] >= 0) dp[i+1][1] = max(dp[i+1][1],dp[i][0]+base*g);
                    }
                }
            }
        }
        base <<= 1;
    }
    cout << dp[n][1] << endl;
    return 0;
}