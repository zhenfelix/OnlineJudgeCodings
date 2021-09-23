class TreeAncestor {
public:
    vector<int> tin, mp;
    vector<vector<int>> level, graph;
    int clock;
    void dfs(int cur, int depth){
        mp[cur] = depth;
        tin[cur] = clock++; 
        level[depth].push_back(cur);
        for (auto nxt : graph[cur])
            dfs(nxt,depth+1);
    }
    TreeAncestor(int n, vector<int>& parent) {
        clock = 0;
        mp.resize(n);
        tin.resize(n);
        level.resize(n);
        graph.resize(n);
        for (int i = 0; i < n; i++){
            if (parent[i] >= 0)
                graph[parent[i]].push_back(i);
        }
        dfs(0,0);
    }
    
    int getKthAncestor(int node, int k) {
        if (k > mp[node])
            return -1;
        vector<int> &vs = level[mp[node]-k];
        int m = vs.size();
        int lo = 0, hi = m-1;  
        while (lo <= hi){
            int mid = (lo+hi)/2;
            if (tin[vs[mid]] > tin[node])
                hi = mid-1;
            else
                lo = mid+1;
        }
        return vs[hi];
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */


















class TreeAncestor {
public:
    vector<vector<int>> ancestor, graph;
    int m;
    void dfs(int cur){
        for (int i = 0;ancestor[cur][i] != -1;i++){
            ancestor[cur][i+1] = ancestor[ancestor[cur][i]][i];
        }
        for (auto nxt : graph[cur])
            dfs(nxt);
    }
    TreeAncestor(int n, vector<int>& parent) {
        for (m=0;(1<<m) <= n;m++){}
        m++;
        ancestor.assign(n,vector<int>(m,-1));
        graph.resize(n);
        for (int i = 0; i < n; i++){
            if (parent[i] >= 0)
                graph[parent[i]].push_back(i);
            ancestor[i][0] = parent[i];
        }
        dfs(0);
    }
    
    int getKthAncestor(int node, int k) {
        for (int i = m-1;i>=0&&node != -1;i--){
            if (k >= (1<<i)){
                node = ancestor[node][i];
                k -= (1<<i);
            }
        }
        return node;
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */