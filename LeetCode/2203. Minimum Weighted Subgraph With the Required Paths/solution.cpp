using ll = long long;

const ll INF = 1e12;

class Solution {
    vector<ll> dijkstra(vector<vector<pair<int, int>>> &adj, int s) {
        int n = adj.size();
        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
        vector<ll> dis(n, INF);
        dis[s] = 0;
        pq.emplace(0, s);
        
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (d > dis[u])
                continue;
            
            for (auto [v, w] : adj[u]) {
                if (d + w < dis[v]) {
                    dis[v] = d + w;
                    pq.emplace(dis[v], v);
                }
            }
        }
        
        return dis;
    }
    
public:
    long long minimumWeight(int n, vector<vector<int>>& edges, int src1, int src2, int dest) {
        vector<vector<pair<int, int>>> adj(n), rev(n);
        for (auto &e : edges) {
            adj[e[0]].emplace_back(e[1], e[2]);
            rev[e[1]].emplace_back(e[0], e[2]);
        }
        
        auto da = dijkstra(adj, src1);
        auto db = dijkstra(adj, src2);
        auto dt = dijkstra(rev, dest);
        
        ll ans = INF;
        for (int i = 0; i < n; ++i)
            ans = min(ans, da[i] + db[i] + dt[i]);
        
        return ans == INF ? -1 : ans;
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/3PMerp/view/yboIva/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。