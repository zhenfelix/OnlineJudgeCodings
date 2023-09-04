using ii = pair<int, int>;

const int N = 1e4 + 10;
const int K = 16;
const int W = 26;
vector<ii> a[N];
int dep[N], f[N][K];
array<int, W> dp[N];
void DFS(int u, int parent = -1) {
  f[u][0] = parent;
  for (int k = 1; k < K; ++k) {
    int v = f[u][k - 1];
    f[u][k] = v < 0 ? -1 : f[v][k - 1];
  }
  dep[u] = parent < 0 ? 0 : dep[parent] + 1;
  for (auto& [v, w] : a[u]) {
    if (v == parent) continue;
      dp[v] = dp[u];
      dp[v][w - 1]++;
    DFS(v, u);
  }
}
int go(int u, int step) {
  for (int k = 0; k < K; ++k) {
    if ((step >> k) & 1) u = u < 0 ? -1 : f[u][k];
  }
  return u;
}
int LCA(int u, int v) {
  if (dep[u] < dep[v]) swap(u, v);
  u = go(u, dep[u] - dep[v]);
  if (u == v) return u;
  for (int k = K - 1; k >= 0; --k) {
    if (f[u][k] != f[v][k]) {
      u = f[u][k]; v = f[v][k];
    }
  }
  return f[u][0];
}

class Solution {
public:
    vector<int> minOperationsQueries(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        for (int i = 0; i < n; ++i) {
            a[i].clear();
            for (int k = 0; k < W; ++k) dp[i][k] = 0;
        }
        for (auto& v : edges) {
            int x = v[0], y = v[1], z = v[2];
            a[x].push_back({y, z});
            a[y].push_back({x, z});
        }
        DFS(0, -1);
        vector<int> ret;
        for (auto& v : queries) {
            int x = v[0], y = v[1], z = LCA(x, y);
            array<int, W> cnt {};
            for (int k = 0; k < W; ++k) {
                cnt[k] = dp[x][k] + dp[y][k] - 2 * dp[z][k];
            }
            int mx = *max_element(cnt.begin(), cnt.end());
            int sum = accumulate(cnt.begin(), cnt.end(), 0);
            ret.push_back(sum - mx);
        }
        return ret;
    }
};

