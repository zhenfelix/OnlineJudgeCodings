#include<bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("input","r",stdin);
    int n, m, e;
    cin >> n >> m >> e;
    int a, b;
    vector<vector<int>> gs(n);
    while (e--) {
        cin >> a >> b;
        a--;b--;
        gs[a].push_back(b);
    }
    vector<int> matched(m,-1), checked(m,0);
    function<bool(int)> dfs = [&] (int u) -> bool {
        for (auto v : gs[u]) {
            if (checked[v]) continue;
            checked[v] = 1;
            if (matched[v] == -1 || dfs(matched[v])) {
                matched[v] = u;
                return true;
            }
        }
        return false;
    };
    int ans = 0;
    for (int i = 0; i < n; i++) {
        checked.assign(m,0);
        if (dfs(i)) ans++;
    }
    cout << ans << endl;
    return 0;
}