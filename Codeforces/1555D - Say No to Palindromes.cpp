#include<bits/stdc++.h>

using namespace std;

int main(){
    // freopen("contests/input","r",stdin);
    int n, m;
    cin >> n >> m;
    string s;
    cin >> s;
    vector<string> patterns {"abc","acb","bac","bca","cab","cba"};
    vector<vector<int>> dp(6,vector<int>(n+1));
    for (int t = 0; t < 6; t++){
        for (int i = 0; i < n; i++) {
            dp[t][i+1] = dp[t][i] + (s[i] != patterns[t][i%3]);
        }
    }
    while (m--)
    {
        int l, r;
        cin >> l >> r;
        int ans = n;
        for (int t = 0; t < 6; t++){
            ans = min(ans, dp[t][r]-dp[t][l-1]);
        }
        cout << ans << endl;
    }
    
}