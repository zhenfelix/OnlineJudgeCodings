class Solution {
    unordered_map<int, vector<int>> con;
    unordered_map<int, vector<pair<int, int>>> nxt;
    
    vector<int> best;
    vector<int> now;
    unordered_map<int, bool> vis;
    int change, end, bc;
    
    void dfs(int u, int i) {        
        if (u == end) {
            if (change < bc || (change == bc && now < best)) {
                bc = change;
                best = now;
            }
            return;
        }
        
        for (auto [v, j] : nxt[u]) {
            if (!vis[v]) {
                int extra = i != j;
                change += extra;
                if (change < bc || (change == bc && now < best)) {
                    now.push_back(v);
                    vis[v] = true;
                    dfs(v, j);
                    vis[v] = false;
                    now.pop_back();
                }
                change -= extra;
            }
        }
    }
    
public:
    vector<int> metroRouteDesignI(vector<vector<int>>& lines, int start, int end) {
        this->end = end;
        int n = lines.size();
        vector<unordered_set<int>> adj(n);
        
        for (int i = 0; i < lines.size(); ++i) {
            int m = lines[i].size();
            for (int stop : lines[i]) {
                con[stop].push_back(i);
            }
            for (int j = 0; j + 1 < m; ++j) {
                int u = lines[i][j], v = lines[i][j + 1];
                nxt[u].emplace_back(v, i);
                nxt[v].emplace_back(u, i);
            }
        }
        
//         for (auto [stop, v] : con) {
//             int m = v.size();
//             if (m >= 2) {
//                 for (int i = 0; i < m; ++i) {
//                     int p = v[i];
//                     for (int j = i + 1; j < m; ++j) {
//                         int q = v[j];
//                         adj[p].insert(q);
//                         adj[q].insert(p);
//                     }
//                 }
//             }
//         }
        
        best = vector<int>(1, 1e9);
        change = 0;
        bc = 1e9;
        now.push_back(start);
        vis[start] = true;
        for (int line : con[start]) {
            dfs(start, line);
        }
        
        return best;
    }
};