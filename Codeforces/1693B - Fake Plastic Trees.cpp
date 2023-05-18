#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    int n;
    cin>>n;
    vector<vector<int>> g(n);
    vector<ll> l(n), r(n), ans(n,0);
    for (int i = 1; i < n; i++) {
        int p;
        cin >> p;
        p--;
        g[p].push_back(i);
    }
    for (int i = 0; i < n; i++) {
        cin >> l[i] >> r[i];
    }
    function<ll(int)> dfs = [&] (int cur) {
        ll mx = 0;
        for (auto nxt : g[cur]) {
            mx += dfs(nxt);
            ans[cur] += ans[nxt];
        }
        if (mx < l[cur]) {
            ans[cur] += 1;
            mx = r[cur];
        }
        return min(mx,r[cur]);
    };
    dfs(0);
    cout << ans[0] << endl;
    return;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    // freopen("contests/input","r",stdin);
    int t;
    cin>>t;
    while(t--){
        solve();
    }
    cout.flush();
    return 0;
}
