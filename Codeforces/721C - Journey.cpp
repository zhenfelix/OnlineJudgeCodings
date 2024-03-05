
#include <bits/stdc++.h>

using namespace std;
using ll = long long;

const ll MOD = 1e9+7;
const int nmax = 5005;

int inf=0x3f3f3f3f;

vector<vector<int>> dp(nmax,vector<int>(nmax,inf));
vector<vector<int>> pre(nmax,vector<int>(nmax,-1));

void solve() {
    int n,m,tmax;
    cin >> n >> m >> tmax;
    vector<tuple<int,int,int>> edges;
    for (int i = 0; i < m; ++i){
        int u,v,w;
        cin >> u >> v >> w;
        edges.emplace_back(u,v,w);
    }
    for(int i = 0; i <= n; ++i)for(int j = 0; j <= n; ++j){
        dp[i][j] = inf;
        pre[i][j] = -1;
    }
    dp[1][0] = 0;
    for (int k = 1; k <= n; ++k) {
        for (auto [u,v,w] : edges) {
            if (dp[u][k-1]+w < dp[v][k]){
                dp[v][k] = dp[u][k-1]+w;
                pre[v][k] = u;
            }
        }
    }
    for (int k = n; k > 0; --k) {
        if (dp[n][k] <= tmax) {
            cout << k+1 << endl;
            vector<int> ans{n};
            for (int i = k; i > 0; --i) {
                ans.push_back(pre[ans.back()][i]);
            }
            reverse(ans.begin(),ans.end());
            for (int i = 0; i <= k; ++i) {
                cout << ans[i];
                if (i < k) cout << " ";
            }
            cout << endl;
            return;
        }
    }
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
