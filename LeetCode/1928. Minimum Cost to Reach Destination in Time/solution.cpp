// const int INF = 0x3f3f3f3f;

// class Solution {
// public:
//     int minCost(int maxTime, vector<vector<int>>& edges, vector<int>& passingFees) {
//         int n = passingFees.size();
//         vector<unordered_map<int, int>> adj(n);
//         for (auto &edge : edges) {
//             int u = edge[0], v = edge[1], w = edge[2];
//             if (w > maxTime)
//                 continue;
//             if (!adj[u].count(v) || adj[u][v] > w)
//                 adj[u][v] = w;
//             if (!adj[v].count(u) || adj[v][u] > w)
//                 adj[v][u] = w;
//         }
        
//         int T = maxTime + 1;
//         vector<int> dis(n * T + 1, INF);
//         dis[0] = passingFees[0];
//         priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
//         pq.emplace(dis[0], 0);
//         while (!pq.empty()) {
//             auto [d, idx] = pq.top();
//             pq.pop();
//             int u = idx / T, t = idx % T;
//             if (d > dis[idx] || t > maxTime)
//                 continue;
            
//             for (auto [v, w] : adj[u]) {
//                 if (t + w < T) {
//                     int nxt = v * T + t + w;
//                     if (d + passingFees[v] < dis[nxt] && t+w <= maxTime) {
//                         dis[nxt] = d + passingFees[v];
//                         pq.emplace(dis[nxt], nxt);
//                     }
//                 }
//             }
//         }
//         int ans = INF;
//         for (int t = 0; t < T; ++t)
//             ans = min(ans, dis[(n - 1) * T + t]);
        
//         return ans == INF ? -1 : ans;
//     }
// };


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/KASKbW/view/tTVV3q/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution {
private:
    // 极大值
    static constexpr int INFTY = INT_MAX / 2;

public:
    int minCost(int maxTime, vector<vector<int>>& edges, vector<int>& passingFees) {
        int n = passingFees.size();
        vector<vector<int>> f(maxTime + 1, vector<int>(n, INFTY));
        f[0][0] = passingFees[0];
        for (int t = 1; t <= maxTime; ++t) {
            for (const auto& edge: edges) {
                int i = edge[0], j = edge[1], cost = edge[2];
                if (cost <= t) {
                    f[t][i] = min(f[t][i], f[t - cost][j] + passingFees[i]);
                    f[t][j] = min(f[t][j], f[t - cost][i] + passingFees[j]);
                }
            }
        }

        int ans = INFTY;
        for (int t = 1; t <= maxTime; ++t) {
            ans = min(ans, f[t][n - 1]);
        }
        return ans == INFTY ? -1 : ans;
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/minimum-cost-to-reach-destination-in-time/solution/gui-ding-shi-jian-nei-dao-da-zhong-dian-n3ews/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。