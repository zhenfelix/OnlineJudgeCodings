class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<int> deg(n);
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            deg[e[1]]++;
            adj[e[0]].push_back(e[1]);
        }
        
        vector<bitset<1000>> ans(n);
        queue<int> q;
        for (int i = 0; i < n; ++i)
            if (deg[i] == 0)
                q.push(i);
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                ans[v] |= ans[u];
                ans[v].set(u);
                deg[v]--;
                if (deg[v] == 0)
                    q.push(v);
            }
        }
        
        vector<vector<int>> result(n);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (ans[i][j])
                    result[i].push_back(j);
        
        return result;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/9WhoB7/view/s15EHo/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。