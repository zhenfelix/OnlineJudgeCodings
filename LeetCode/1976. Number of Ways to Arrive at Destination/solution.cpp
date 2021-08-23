using ll = long long;
const ll MOD = 1e9 + 7;

class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        vector<vector<pair<int, int>>> adj(n);
        for (auto &road : roads) {
            int u = road[0], v = road[1], t = road[2];
            adj[u].emplace_back(v, t);
            adj[v].emplace_back(u, t);
        }
        
        vector<ll> dis(n, LLONG_MAX), ways(n);
        dis[0] = 0;
        ways[0] = 1;
        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
        pq.emplace(0, 0);
        while (!pq.empty()) {
            auto [t, u] = pq.top();
            pq.pop();
            if (t > dis[u])
                continue;
            for (auto [v, w] : adj[u]) {
                if (t + w < dis[v]) {
                    dis[v] = t + w;
                    ways[v] = 0;
                    pq.emplace(t + w, v);
                }
                if (t + w == dis[v])
                    ways[v] = (ways[v] + ways[u]) % MOD;
            }
        }
        
        return ways[n - 1];
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/paT4GG/view/ARvu3X/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。