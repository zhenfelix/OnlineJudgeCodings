#include <bits/stdc++.h>

using namespace std;
using i64 = int64_t;
using f64 = double_t;
using pii = pair<int,int>;

void solve() {
  int n;
  cin >> n;
  vector<int> arr(n),parent(n), sz(n,1), g(n,0);
  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
    arr[i]--;
    parent[i] = i;
  }
  function<int(int)> find = [&] (int cur) -> int {
    if (parent[cur] != cur) parent[cur] = find(parent[cur]);
    return parent[cur];
  };
  function<void(int,int)> connect = [&] (int u, int v) {
    int ru = find(u), rv = find(v);
    if (ru != rv) {
      parent[rv] = ru;
      sz[ru] += sz[rv];
    }
  };  
  for (int i = 0; i < n; ++i) connect(i,arr[i]);
  for (int i = 0; i < n; ++i) {
    int j = find(i);
    g[j] = sz[j];
  }
  int ans = 0;
  for (int i = 0; i < n; ++i) if (g[i]) ans += g[i]-1;
  for (int i = 0; i < n-1; ++i) if (find(i) == find(i+1)) {
    cout << ans-1 << endl;
    return;
  }
  cout << ans+1 << endl;
  return;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
#ifndef ONLINE_JUDGE 
    freopen("input","r",stdin);
#endif
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}
