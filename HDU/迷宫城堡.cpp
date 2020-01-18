#include<bits/stdc++.h>
using namespace std;
const int N = 10100;
struct Tarjan_Scc {
    stack<int>s;
    bool instack[N];
    struct edge { int to, next; }G[N * 10];
    int scc, idx, tot, dfn[N], low[N], head[N];
    inline void init(int n) {
        scc = tot = idx = 0;
        while (!s.empty()) s.pop();
        for (int i = 0; i < n + 2; i++) {
            head[i] = -1;
            instack[i] = false;
            dfn[i] = low[i] = 0;
        }
    }
    inline void add_edge(int u, int v) {
        G[tot].to = v, G[tot].next = head[u], head[u] = tot++;
    }
    inline void built(int m) {
        int u, v;
        while (m--) {
            scanf("%d %d", &u, &v);
            add_edge(u, v);
        }
    }
    inline void tarjan(int u) {
        dfn[u] = low[u] = ++idx;
        s.push(u);
        instack[u] = true;
        for (int i = head[u]; ~i; i = G[i].next) {
            int &v = G[i].to;
            if (!dfn[v]) {
                tarjan(v);
                low[u] = min(low[u], low[v]);
            } else if (instack[v] && dfn[v] < low[u]) {
                // low[u] = low[v];
                low[u] = dfn[v];
            }
        }
        if (low[u] == dfn[u]) {
            scc++;
            int v = 0;
            do {
                v = s.top(); s.pop();
                instack[v] = false;
            } while (v != u);
        }
    }
    inline void solve(int n, int m) {
        init(n);
        built(m);
        for (int i = 1; i <= n; i++) {
            if (!dfn[i]) tarjan(i);
        }
        puts(scc == 1 ? "Yes" : "No");
    }
}go;
int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w+", stdout);
#endif
    
    int n, m;
    while (~scanf("%d %d", &n, &m), m + n) {
        go.solve(n, m);
    }
    return 0;
}





#include<bits/stdc++.h>
using namespace std;
const int maxn = 1e4 + 5;

vector<int> g[maxn], rg[maxn];  // 原图和反图
vector<int> s;  // 时间戳
int vis[maxn];
int sccno[maxn];
int cnt;  // 强连通分量的个数

void init(int n) {
    for(int i = 0; i < n; ++i) {
        g[i].clear();
        rg[i].clear();
    }
    cnt = 0;
    s.clear();
    memset(sccno, 0, sizeof(sccno));
    memset(vis, 0, sizeof(vis));
}

void dfs1(int u) {
    if(vis[u]) return;
    vis[u] = 1;
    for(int i = 0; i < g[u].size(); ++i) {
        dfs1(g[u][i]);
    }
    s.push_back(u);
}

void dfs2(int u) {
    if(sccno[u]) return;
    sccno[u] = cnt;
    for(int i = 0; i < rg[u].size(); ++i) {
        dfs2(rg[u][i]);
    }
}

void Kosaraju(int n) {
    for(int i = 1; i <= n; ++i) {
        dfs1(i);
    }
    for(int i = n - 1; ~i; --i) {
        if(!sccno[s[i]]) {
            ++cnt;
            dfs2(s[i]);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m;
    while(cin >> n >> m) {
        if(n == 0 && m == 0) break;
        init(n);
        for(int i = 0; i < m; ++i) {
            int u, v;
            cin >> u >> v;
            g[u].push_back(v);
            rg[v].push_back(u);
        }
        Kosaraju(n);
        cout << (cnt == 1? "Yes": "No") << endl;
    }
    return 0;
}