class Solution {
    int n, max_loop, from_pairs;
    vector<int> color, dep;
    vector<pair<int, int>> pairs;
    vector<vector<int>> rev;
    
    void dfs(int u) {
        color[u] = 1;
        
        for (int v : rev[u]) {
            if (!color[v]) {
                dep[v] = dep[u] + 1;
                dfs(v);
            } else if (color[v] == 1) {
                int loop = dep[u] - dep[v] + 1;
                max_loop = max(max_loop, loop);
                if (loop == 2)
                    pairs.emplace_back(u, v);
            }
        }
        
        color[u] = 2;
    }
    
    int dfs2(int u, int p, int d) {
        int max_depth = d;
        
        for (int v : rev[u]) {
            if (v != p)
                max_depth = max(max_depth, dfs2(v, p, d + 1));
        }

        return max_depth;
    }

public:
    int maximumInvitations(vector<int>& favorite) {
        n = favorite.size();
        color = vector<int>(n);
        dep = vector<int>(n);
        max_loop = 0;
        
        rev = vector<vector<int>>(n);
        for (int i = 0; i < n; ++i)
            rev[favorite[i]].emplace_back(i);
        
        for (int i = 0; i < n; ++i) {
            if (!color[i])
                dfs(i);
        }
        
        from_pairs = 0;
        for (auto &[u, v] : pairs) {
            from_pairs += dfs2(u, v, 1);
            from_pairs += dfs2(v, u, 1);
        }
        
        return max(max_loop, from_pairs);
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/PS7Stz/view/Xe2A1O/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。