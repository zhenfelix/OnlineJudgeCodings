class Solution {
public:
    int numberOfSets(int n, int maxDistance, vector<vector<int>>& roads) {
        int d[n][n];
        memset(d, 0x3f, sizeof(d));
        for(const auto& r : roads) d[r[0]][r[1]]=min(d[r[0]][r[1]], r[2]), d[r[1]][r[0]] = min(d[r[1]][r[0]], r[2]);

        int f[1 << n][n][n], res = 1;
        memset(f, 0x3f, sizeof(f));
        memcpy(f[0], d, sizeof(d));

        for(int m = 1; m < (1 << n); ++m) {
            int k = __builtin_ctz(m), p = (m ^ (1 << k));
            int mx = 0;
            for(int i = 0; i < n; ++i) {
                for(int j = 0; j < n; ++j) {
                    f[m][i][j] = min(f[p][i][j], f[p][i][k] + f[p][k][j]);
                    if(i != j && (m & (1 << i)) && (m & (1 << j))) mx = max(mx, f[m][i][j]);
                }
            }
            if(mx <= maxDistance) ++res;
        }

        return res;
    }
};

// 作者：newhar
// 链接：https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

// Skyqwq
#include <bits/stdc++.h>

#define pb push_back
#define fi first
#define se second
#define mp make_pair

using namespace std;

typedef pair<int, int> PII;
typedef long long LL;

template <typename T> bool chkMax(T &x, T y) { return (y > x) ? x = y, 1 : 0; }
template <typename T> bool chkMin(T &x, T y) { return (y < x) ? x = y, 1 : 0; }

class Solution {
public:

    int d[10][10];
    int numberOfSets(int n, int w, vector<vector<int>>& e) {
       int ans = 0;
       for (int s = 0; s < (1 << n); s++) {
            memset(d, 0x3f, sizeof d);
            for (int j = 0; j < n; j++) d[j][j] = 0;
            for (auto o: e) {
                int u = o[0], v = o[1], w = o[2];
                if ((s >> u & 1) && (s >> v & 1)) {
                    chkMin(d[u][v], w);
                    chkMin(d[v][u], w);
                }
            }
            for (int k = 0; k < n; k++) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        chkMin(d[i][j], d[i][k] + d[k][j]);
                    }
                }
            }
            bool ok = 1;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if ((s >> i & 1) && (s >> j & 1)) {
                        if (d[i][j] > w) {
                            ok = 0;
                        }
                    }
                }
            }
            if (ok) ans++;
       }
       return ans; 
    }
};

class Solution {
public:
    int numberOfSets(int n, int maxDistance, vector<vector<int>>& roads) {
        vector<int> e[n], v[n];
        for (auto &road : roads) {
            e[road[0]].push_back(road[1]); v[road[0]].push_back(road[2]);
            e[road[1]].push_back(road[0]); v[road[1]].push_back(road[2]);
        }
        bool ban[n];

        typedef pair<long long, int> pli;
        auto dijkstra = [&](int S) {
            long long dis[n];
            memset(dis, -1, sizeof(dis));
            priority_queue<pli> pq;
            pq.push(pli(0, S));
            while (pq.size() > 0) {
                pli p = pq.top(); pq.pop();
                int sn = p.second;
                if (dis[sn] >= 0) continue;
                dis[sn] = -p.first;
                for (int i = 0; i < e[sn].size(); i++) {
                    int fn = e[sn][i];
                    if (!ban[fn] && dis[fn] < 0) pq.push(pli(-dis[sn] - v[sn][i], fn));
                }
            }

            long long ret = 0;
            for (int i = 0; i < n; i++) if (!ban[i]) {
                if (dis[i] < 0) return maxDistance + 1LL;
                else ret = max(ret, dis[i]);
            }
            return ret;
        };

        auto gao = [&](int msk) {
            for (int i = 0; i < n; i++) ban[i] = msk >> i & 1;
            for (int i = 0; i < n; i++) if (!ban[i]) {
                long long t = dijkstra(i);
                if (t > maxDistance) return false;
            }
            return true;
        };

        int ans = 0;
        for (int i = 0; i < (1 << n); i++) if (gao(i)) ans++;
        return ans;
    }
};


using ii = pair<int, int>;
class Solution {
public:
    int numberOfSets(int n, int D, vector<vector<int>>& roads) {
        vector<vector<ii>> a(n);
        for (auto& v : roads) {
            int x = v[0], y = v[1], z = v[2];
            a[x].push_back({y, z});
            a[y].push_back({x, z});
        }
        int ret = 0;
        for (int mask = 0; mask < (1 << n); ++mask) {   
            vector<int> v;
            for (int i = 0; i < n; ++i) {
                if ((mask >> i) & 1) continue;
                v.push_back(i);
            }
            int len = v.size();
            auto dijkstra = [&](int s) {
                priority_queue<ii, vector<ii>, greater<>> pq;
                vector<int> d(n, 1e9);
                d[s] = 0;
                pq.push({d[s], s});
                while (!pq.empty()) {
                    auto [dd, u] = pq.top();
                    pq.pop();
                    if (dd != d[u]) continue;
                    for (auto& [v, w] : a[u]) {
                        if ((mask >> v) & 1) continue;
                        if (d[v] > d[u] + w) {
                            d[v] = d[u] + w;
                            pq.push({d[v], v});
                        }
                    }
                }
                return d;
            };
            bool ok = 1;
            for (int i = 0; i < len; ++i) {
                const auto& d = dijkstra(v[i]);
                for (int j = 0; j < len; ++j) {
                    if (d[v[j]] > D) ok = 0;
                }
                if (!ok) break;
            }
            if (ok) ++ret;
        }
        return ret;
    }
};