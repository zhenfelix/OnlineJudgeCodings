#include<bits/stdc++.h>

using namespace std;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input","r",stdin);
    #endif
    int n, v, m, l, r;
    cin >> n;
    vector<vector<int>> mp(n+1,vector<int>());
    for (int i = 1; i <= n; i++) {
        cin >> v;
        mp[v].push_back(i);
    }
    cin >> m;
    for (int i = 1 ; i <= m; i++) {
        cin >> l >> r >> v;
        auto hi = upper_bound(mp[v].begin(), mp[v].end(),r);
        auto lo = lower_bound(mp[v].begin(), mp[v].end(),l);
        cout << hi-lo << endl;
    }
    
    return 0;
}