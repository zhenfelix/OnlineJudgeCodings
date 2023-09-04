
#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("input","r",stdin);
    int n;
    cin >> n;
    vector<string> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<vector<int>> dp(26,vector<int>(26,0));
    int ans = 0;
    for (int k = 0; k < n; k++){
        int sz = arr[k].length();
        int last = arr[k].back()-'a';
        int j = arr[k][0]-'a';
        vector<int> tmp(26);
        for (int i = 0; i < 26; i++) {
            if (dp[i][j] > 0 || i == j) tmp[i] = dp[i][j]+sz;
        }
        for (int i = 0; i < 26; i++) {
            dp[i][last] = max(dp[i][last],tmp[i]);
            if (i == last) ans = max(ans,dp[i][last]);
        }
    }
    cout << ans << endl;
    return 0;
}