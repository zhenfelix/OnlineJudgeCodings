const int inf = 0x3f3f3f3f;

class Solution {
    int n,m;
    vector<int> parent;
    int mst_remove(int i, vector<int> &idx, vector<vector<int>>& edges){
        parent.resize(n);
        for (int j = 0; j < n; j++)
            parent[j] = j;
        return mst(i,idx,edges);
    }
    int mst_add(int i, vector<int> &idx, vector<vector<int>>& edges){
        parent.resize(n);
        for (int j = 0; j < n; j++)
            parent[j] = j;
        connect(edges[i][0],edges[i][1]);
        return mst(i,idx,edges)+edges[i][2];
    }
    int mst(int i, vector<int> &idx, vector<vector<int>>& edges){
        int w = 0;
        for (auto j : idx){
            if (j == i)
                continue;
            if (connect(edges[j][0], edges[j][1]))
                w += edges[j][2];
        }
        for (int j = 1; j < n; j++)
            if (find(j) != find(j-1))
                return inf;
        return w;
    }

    int find(int root){
        if (parent[root] != root)
            parent[root] = find(parent[root]);
        return parent[root];
    }
    bool connect(int u, int v){
        int ru = find(u), rv = find(v);
        if (ru != rv){
            parent[ru] = rv;
            return true;
        }
        return false;
    }

public:
    
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        int m = edges.size();
        this->n = n;
        this->m = m;
        vector<int> idx;
        for (int i = 0; i < m; i++)
            idx.push_back(i);
        sort(idx.begin(), idx.end(), [&](int a, int b){
            return edges[a][2] < edges[b][2];
        });
        int wt = mst_remove(-1,idx,edges);
        vector<vector<int>> res(2);
        for (int i = 0; i < m; i++){
            if (mst_remove(i,idx,edges) > wt){
                res[0].push_back(i);
                continue;
            }
            if (mst_add(i,idx,edges) == wt){
                res[1].push_back(i);
            }
            // int wc = mst_add(i,idx,edges);
            // if (wc > wt)
            //     continue;
            // wc = mst_remove(i,idx,edges);
            // if (wc > wt)
            //     res[0].push_back(i);
            // else if (wc == wt)
            //     res[1].push_back(i);
        }
        return res;
    }
};









using pp = pair<int,int>;

const int inf = 0x3f3f3f3f;

class Solution {
    int n,m,clock;
    vector<int> parent, label;
    unordered_map<int,int> low, tin;
    unordered_map<int,vector<pp>> graph;

    int find(int root){
        if (parent[root] != root)
            parent[root] = find(parent[root]);
        return parent[root];
    }
    bool connect(int u, int v){
        int ru = find(u), rv = find(v);
        if (ru != rv){
            parent[ru] = rv;
            return true;
        }
        return false;
    }

    void tarjan(int v, int pi){
        tin[v] = low[v] = ++clock;
        for (auto &[u, i] : graph[v]){
            if (i == pi)
                continue;
            if (tin[u] != -1)
                low[v] = min(low[v], tin[u]);
            else{
                tarjan(u, i);
                low[v] = min(low[v], low[u]);
                if (low[u] > tin[v])
                    label[i] = 1;
            }
        }
    }

public:
    
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        int m = edges.size();
        this->n = n;
        this->m = m;
        label.assign(m,0);
        parent.resize(n);
        for (int i = 0; i < n; i++)
            parent[i] = i;
        map<int,vector<int>>mp;
        for (int i = 0; i < m; i++)
            mp[edges[i][2]].push_back(i);
        vector<vector<int>> res(2);
        for (auto &[w, es] : mp){
            clock = 0;
            low.clear();
            tin.clear();
            graph.clear();
            for (auto i : es){
                int u = edges[i][0], v = edges[i][1];
                int ru = find(u), rv = find(v);
                if (ru != rv){
                    graph[ru].push_back({rv,i});
                    graph[rv].push_back({ru,i});
                }
                else
                    label[i] = -1;
            }
            vector<int> vs;
            for (auto &[v, es] : graph)
                vs.push_back(v);
            for (auto v : vs){
                low[v] = -1;
                tin[v] = -1;
            }
            for (auto v : vs)
                if (tin[v] == -1)
                    tarjan(v, -1);
            for (auto i : es){
                int u = edges[i][0], v = edges[i][1];
                connect(u,v);
            }

        }
        for (int i = 0; i < m; i++)
            if (label[i] == 1)
                res[0].push_back(i);
            else if (label[i] == 0)
                res[1].push_back(i);
        return res;
    }
};
























// 并查集模板
class UnionFind {
public:
    vector<int> parent;
    vector<int> size;
    int n;
    // 当前连通分量数目
    int setCount;
    
public:
    UnionFind(int _n): n(_n), setCount(_n), parent(_n), size(_n, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    
    int findset(int x) {
        return parent[x] == x ? x : parent[x] = findset(parent[x]);
    }
    
    bool unite(int x, int y) {
        x = findset(x);
        y = findset(y);
        if (x == y) {
            return false;
        }
        if (size[x] < size[y]) {
            swap(x, y);
        }
        parent[y] = x;
        size[x] += size[y];
        --setCount;
        return true;
    }
    
    bool connected(int x, int y) {
        x = findset(x);
        y = findset(y);
        return x == y;
    }
};

// Tarjan 算法求桥边模版
class TarjanSCC {
private:
    const vector<vector<int>>& edges;
    const vector<vector<int>>& edgesId;
    vector<int> low;
    vector<int> dfn;
    vector<int> ans;
    int n;
    int ts;

private:
    void getCuttingEdge_(int u, int parentEdgeId) {
        low[u] = dfn[u] = ++ts;
        for (int i = 0; i < edges[u].size(); ++i) {
            int v = edges[u][i];
            int id = edgesId[u][i];
            if (dfn[v] == -1) {
                getCuttingEdge_(v, id);
                low[u] = min(low[u], low[v]);
                if (low[v] > dfn[u]) {
                    ans.push_back(id);
                }
            }
            else if (id != parentEdgeId) {
                low[u] = min(low[u], dfn[v]);
            }
        }
    }

public:
    TarjanSCC(int n_, const vector<vector<int>>& edges_, const vector<vector<int>>& edgesId_): \
        edges(edges_), edgesId(edgesId_), low(n_, -1), dfn(n_, -1), n(n_), ts(-1) {}
    
    vector<int> getCuttingEdge() {
        for (int i = 0; i < n; ++i) {
            if (dfn[i] == -1) {
                getCuttingEdge_(i, -1);
            }
        }
        return ans;
    }
};

class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        int m = edges.size();
        for (int i = 0; i < m; ++i) {
            edges[i].push_back(i);
        }
        sort(edges.begin(), edges.end(), [](const auto& u, const auto& v) {
            return u[2] < v[2];
        });

        UnionFind uf(n);
        vector<vector<int>> ans(2);
        vector<int> label(m);
        for (int i = 0; i < m;) {
            // 找出所有权值为 w 的边，下标范围为 [i, j)
            int w = edges[i][2];
            int j = i;
            while (j < m && edges[j][2] == edges[i][2]) {
                ++j;
            }

            // 存储每个连通分量在图 G 中的编号
            unordered_map<int, int> compToId;
            // 图 G 的节点数
            int gn = 0;
            
            for (int k = i; k < j; ++k) {
                int x = uf.findset(edges[k][0]);
                int y = uf.findset(edges[k][1]);
                if (x != y) {
                    if (!compToId.count(x)) {
                        compToId[x] = gn++;
                    }
                    if (!compToId.count(y)) {
                        compToId[y] = gn++;
                    }
                }
                else {
                    // 将自环边标记为 -1
                    label[edges[k][3]] = -1;
                }
            }
            
            // 图 G 的边
            vector<vector<int>> gm(gn), gmid(gn);
            
            for (int k = i; k < j; ++k) {
                int x = uf.findset(edges[k][0]);
                int y = uf.findset(edges[k][1]);
                if (x != y) {
                    int idx = compToId[x], idy = compToId[y];
                    gm[idx].push_back(idy);
                    gmid[idx].push_back(edges[k][3]);
                    gm[idy].push_back(idx);
                    gmid[idy].push_back(edges[k][3]);
                }
            }

            vector<int> bridges = TarjanSCC(gn, gm, gmid).getCuttingEdge();
            // 将桥边（关键边）标记为 1
            for (int id: bridges) {
                ans[0].push_back(id);
                label[id] = 1;
            }

            for (int k = i; k < j; ++k) {
                uf.unite(edges[k][0], edges[k][1]);
            }

            i = j;
        }

        // 未标记的边即为非桥边（伪关键边）
        for (int i = 0; i < m; ++i) {
            if (!label[i]) {
                ans[1].push_back(i);
            }
        }

        return ans;
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solution/zhao-dao-zui-xiao-sheng-cheng-shu-li-de-gu57q/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。