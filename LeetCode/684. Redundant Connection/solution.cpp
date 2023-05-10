using pii = pair<int,int>;

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<vector<pii>> g(n);
        vector<int> degree(n,0);
        for (int i = 0; i < n; i++) {
            int u = edges[i][0]-1, v = edges[i][1]-1;
            degree[u]++;
            degree[v]++;
            g[u].push_back({v,i});
            g[v].push_back({u,i});
        }
        vector<bool> visited(n,false);
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (degree[i] == 1) q.push(i);
        }
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            for (auto &[nxt,j] : g[cur]) {
                if (!visited[j]) {
                    visited[j] = true;
                    degree[nxt]--;
                    if (degree[nxt] == 1) q.push(nxt);
                }
            }
        }
        for (int i = n-1; i >= 0; i--) {
            if (!visited[i]) return {edges[i][0],edges[i][1]};
        }
        return {};
    }
};



class Solution {
public:
    int Find(vector<int>& parent, int index) {
        if (parent[index] != index) {
            parent[index] = Find(parent, parent[index]);
        }
        return parent[index];
    }

    void Union(vector<int>& parent, int index1, int index2) {
        parent[Find(parent, index1)] = Find(parent, index2);
    }

    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> parent(n + 1);
        for (int i = 1; i <= n; ++i) {
            parent[i] = i;
        }
        for (auto& edge: edges) {
            int node1 = edge[0], node2 = edge[1];
            if (Find(parent, node1) != Find(parent, node2)) {
                Union(parent, node1, node2);
            } else {
                return edge;
            }
        }
        return vector<int>{};
    }
};

作者：力扣官方题解
链接：https://leetcode.cn/problems/redundant-connection/solutions/557616/rong-yu-lian-jie-by-leetcode-solution-pks2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。