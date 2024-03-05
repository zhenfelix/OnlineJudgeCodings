
#include <bits/stdc++.h>

using namespace std;
using i64 = int64_t;
using f64 = double_t;
using pii = pair<int,int>;

void solve() {
  int n;
  cin >> n;
  vector<vector<pii>> g(n);
  for (int i = 0; i < n-1; ++i) {
    int x,y,w;
    cin >> x >> y >> w;
    x--;y--;w--;
    g[x].push_back({y,w});
    g[y].push_back({x,w});
  }
  vector<int> ans;
  function<bool(int,int)> dfs = [&] (int cur, int pre) -> bool {
    bool flag = false;
    for (auto &[nxt, w] : g[cur]) {
      if (nxt == pre) continue;
      if (w > 0) {
        flag = true;
        if (!dfs(nxt,cur)) ans.push_back(nxt);
      }
      else {
        flag |= dfs(nxt,cur);
      }
    }
    return flag;
  };
  dfs(0,0);
  int m = ans.size();
  cout << m << endl;
  for (int i = 0; i < m; ++i) {
    cout << ans[i]+1;
    if (i < m-1) cout << " ";
  }
  cout << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
#ifndef ONLINE_JUDGE 
    freopen("input","r",stdin);
#endif
  solve();
}
