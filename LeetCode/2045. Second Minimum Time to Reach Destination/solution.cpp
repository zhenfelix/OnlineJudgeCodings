const int INF = 0x3f3f3f3f;

class Solution {
public:
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        vector<vector<int>> adj(n);
        for (auto &edge : edges) {
            int u = edge[0] - 1, v = edge[1] - 1;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        
        queue<int> q;
        vector<int> d(n, INF);
        vector<bool> can(n);
        d[0] = 0;
        q.emplace(0);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (d[u] + 1 < d[v]) {
                    d[v] = d[u] + 1;
                    q.emplace(v);
                } else if (d[u] == d[v] || (can[u] && d[u] < d[v])) {
                    if (!can[v])
                        q.emplace(v);
                    can[v] = true;
                }
            }
        }
        
        int dist = d[n - 1] + 2;
        if (can[n - 1]) 
            dist--;
        
        int t = 0;
        while (dist--) {
            t += time;
            if (dist > 0 && t % (2 * change) >= change)
                t = (t / (2 * change) + 1) * 2 * change;
        }
        
        return t;
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/89Uy1V/view/7QeRXQ/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。