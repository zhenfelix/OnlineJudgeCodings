const int inf = 20005;
vector<pair<int, int>> dirs = {{-1, 0}, {0, -1}};
struct Edge
{
    int from, to, cap;
    Edge(int f, int t, int c)
        : from(f), to(t), cap(c)
    {
    }
};

class Solution
{
public:
    void addEdge(int from, int to, int cap, vector<vector<int>> &graph, vector<Edge> &edges)
    {
        edges.emplace_back(from, to, cap);
        graph[from].push_back(edges.size() - 1);
    }
    void connect(int a, int b, vector<vector<int>> &graph, vector<Edge> &edges)
    {
        addEdge(a * 2 + 1, b * 2, inf, graph, edges);
        addEdge(b * 2, a * 2 + 1, 0, graph, edges);
        addEdge(b * 2 + 1, a * 2, inf, graph, edges);
        addEdge(a * 2, b * 2 + 1, 0, graph, edges);
    }

    int bfs(int start, int aim, vector<vector<int>> &graph, vector<Edge> &edges)
    {
        bool reach = false;
        int delta = inf;
        vector<int> parent(graph.size(), -1);
        queue<pair<int, int>> q;
        parent[start] = inf;
        q.push({start, inf});
        while (!q.empty())
        {
            auto [cur, new_flow] = q.front();
            q.pop();
            if (cur == aim)
            {
                reach = true;
                delta = new_flow;
                break;
            }
            for (auto idx : graph[cur])
            {
                int to = edges[idx].to;
                int cap = edges[idx].cap;
                if (cap && parent[to] == -1)
                {
                    parent[to] = idx;
                    q.push({to, min(new_flow, cap)});
                }
            }
        }
        if (!reach)
            return 0;
        for (int cur = aim; cur != start; cur = edges[parent[cur]].from)
        {
            edges[parent[cur]].cap -= delta;
            edges[parent[cur] ^ 1].cap += delta;
        }
        return delta;
    }

    int MaxFlow(int start, int aim, vector<vector<int>> &graph, vector<Edge> &edges)
    {
        int flow = 0;
        while (int delta = bfs(start, aim, graph, edges))
        {
            flow += delta;
            if (flow >= inf)
                return -1;
        }
        return flow;
    }

    int guardCastle(vector<string> &grid)
    {
        int castle, n = grid[0].size();
        int demon = n * 4 + 1, port = n * 4 + 2;
        vector<vector<int>> graph(n*4+5, vector<int>());
        vector<Edge> edges;
        for (int i = 0; i < 2; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == '#')
                    continue;
                else
                {
                    for (auto [di, dj] : dirs)
                    {
                        di += i;
                        dj += j;
                        if (0 <= di && di < 2 && 0 <= dj && dj < n && grid[di][dj] != '#')
                        {
                            connect(i * n + j, di * n + dj, graph, edges);
                        }
                    }
                    if (grid[i][j] == '.')
                    {
                        addEdge((i * n + j) * 2 + 1, (i * n + j) * 2, 0, graph, edges);
                        addEdge((i * n + j) * 2, (i * n + j) * 2 + 1, 1, graph, edges);
                    }
                    else if (grid[i][j] == 'P')
                    {
                        addEdge(port, (i * n + j) * 2, 0, graph, edges);
                        addEdge((i * n + j) * 2, port, inf, graph, edges);
                        addEdge(port, (i * n + j) * 2 + 1, inf, graph, edges);
                        addEdge((i * n + j) * 2 + 1, port, 0, graph, edges);
                    }
                    else if (grid[i][j] == 'S')
                    {
                        addEdge((i * n + j) * 2, demon, inf, graph, edges);
                        addEdge(demon, (i * n + j) * 2, 0, graph, edges);
                    }
                    else if (grid[i][j] == 'C')
                    {
                        addEdge((i * n + j) * 2 + 1, (i * n + j) * 2, 0, graph, edges);
                        addEdge((i * n + j) * 2, (i * n + j) * 2 + 1, inf, graph, edges);
                        castle = (i * n + j) * 2;
                    }
                }
            }
        }

        return MaxFlow(castle, demon, graph, edges);
    }
};


















namespace atcoder {

namespace internal {

template <class T> struct simple_queue {
    std::vector<T> payload;
    int pos = 0;
    void reserve(int n) { payload.reserve(n); }
    int size() const { return int(payload.size()) - pos; }
    bool empty() const { return pos == int(payload.size()); }
    void push(const T& t) { payload.push_back(t); }
    T& front() { return payload[pos]; }
    void clear() {
        payload.clear();
        pos = 0;
    }
    void pop() { pos++; }
};

}  // namespace internal

}  // namespace atcoder

namespace atcoder {

template <class Cap> struct mf_graph {
  public:
    mf_graph() : _n(0) {}
    explicit mf_graph(int n) : _n(n), g(n) {}

    int add_edge(int from, int to, Cap cap) {
        // printf("edge = %d %d %d\n", from, to, cap);
        assert(0 <= from && from < _n);
        assert(0 <= to && to < _n);
        assert(0 <= cap);
        int m = int(pos.size());
        pos.push_back({from, int(g[from].size())});
        int from_id = int(g[from].size());
        int to_id = int(g[to].size());
        if (from == to) to_id++;
        g[from].push_back(_edge{to, to_id, cap});
        g[to].push_back(_edge{from, from_id, 0});
        return m;
    }

    struct edge {
        int from, to;
        Cap cap, flow;
    };

    edge get_edge(int i) {
        int m = int(pos.size());
        assert(0 <= i && i < m);
        auto _e = g[pos[i].first][pos[i].second];
        auto _re = g[_e.to][_e.rev];
        return edge{pos[i].first, _e.to, _e.cap + _re.cap, _re.cap};
    }
    std::vector<edge> edges() {
        int m = int(pos.size());
        std::vector<edge> result;
        for (int i = 0; i < m; i++) {
            result.push_back(get_edge(i));
        }
        return result;
    }
    void change_edge(int i, Cap new_cap, Cap new_flow) {
        int m = int(pos.size());
        assert(0 <= i && i < m);
        assert(0 <= new_flow && new_flow <= new_cap);
        auto& _e = g[pos[i].first][pos[i].second];
        auto& _re = g[_e.to][_e.rev];
        _e.cap = new_cap - new_flow;
        _re.cap = new_flow;
    }

    Cap flow(int s, int t) {
        return flow(s, t, std::numeric_limits<Cap>::max());
    }
    Cap flow(int s, int t, Cap flow_limit) {
        assert(0 <= s && s < _n);
        assert(0 <= t && t < _n);
        assert(s != t);

        std::vector<int> level(_n), iter(_n);
        internal::simple_queue<int> que;

        auto bfs = [&]() {
            std::fill(level.begin(), level.end(), -1);
            level[s] = 0;
            que.clear();
            que.push(s);
            while (!que.empty()) {
                int v = que.front();
                que.pop();
                for (auto e : g[v]) {
                    if (e.cap == 0 || level[e.to] >= 0) continue;
                    level[e.to] = level[v] + 1;
                    if (e.to == t) return;
                    que.push(e.to);
                }
            }
        };
        auto dfs = [&](auto self, int v, Cap up) {
            if (v == s) return up;
            Cap res = 0;
            int level_v = level[v];
            for (int& i = iter[v]; i < int(g[v].size()); i++) {
                _edge& e = g[v][i];
                if (level_v <= level[e.to] || g[e.to][e.rev].cap == 0) continue;
                Cap d =
                    self(self, e.to, std::min(up - res, g[e.to][e.rev].cap));
                if (d <= 0) continue;
                g[v][i].cap += d;
                g[e.to][e.rev].cap -= d;
                res += d;
                if (res == up) return res;
            }
            level[v] = _n;
            return res;
        };

        Cap flow = 0;
        while (flow < flow_limit) {
            bfs();
            if (level[t] == -1) break;
            std::fill(iter.begin(), iter.end(), 0);
            Cap f = dfs(dfs, t, flow_limit - flow);
            if (!f) break;
            flow += f;
        }
        return flow;
    }

    std::vector<bool> min_cut(int s) {
        std::vector<bool> visited(_n);
        internal::simple_queue<int> que;
        que.push(s);
        while (!que.empty()) {
            int p = que.front();
            que.pop();
            visited[p] = true;
            for (auto e : g[p]) {
                if (e.cap && !visited[e.to]) {
                    visited[e.to] = true;
                    que.push(e.to);
                }
            }
        }
        return visited;
    }

  private:
    int _n;
    struct _edge {
        int to, rev;
        Cap cap;
    };
    std::vector<std::pair<int, int>> pos;
    std::vector<std::vector<_edge>> g;
};

}  // namespace atcoder


class Solution {
private:
    static constexpr int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static constexpr int INF = 20010;
    
public:
    int guardCastle(vector<string>& grid) {
        int n = grid[0].size();
        // extra point for collecting portals & demons
        // portal=n*4, demons=n*4+1
        atcoder::mf_graph<int> g(n * 4 + 2);
        int sx = -1, sy = -1;
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < n; ++j) {
                int base_id = i * n + j;
                if(grid[i][j]=='#') continue;
                if (grid[i][j] == '.') {
                    g.add_edge(base_id * 2, base_id * 2 + 1, 1);
                }
                else if (grid[i][j] == 'C') {
                    g.add_edge(base_id * 2, base_id * 2 + 1, INF);
                    sx = i;
                    sy = j;
                }
                else if (grid[i][j] == 'S' || grid[i][j] == 'P') {
                    g.add_edge(base_id * 2, base_id * 2 + 1, INF);
                }
                
                if (grid[i][j] == 'S') {
                    g.add_edge(base_id * 2 + 1, n * 4 + 1, INF);
                }
                if (grid[i][j] == 'P') {
                    g.add_edge(base_id * 2 + 1, n * 4, INF);
                    g.add_edge(n * 4, base_id * 2, INF);
                }
                for (int d = 0; d < 4; ++d) {
                    int ii = i + dirs[d][0];
                    int jj = j + dirs[d][1];
                    if (ii >= 0 && ii < 2 && jj >= 0 && jj < n) {
                        if (grid[ii][jj] == '#') {
                            continue;
                        }
                        int case_id = ii * n + jj;
                        g.add_edge(base_id * 2 + 1, case_id * 2, INF);
                    }
                }
            }
        }
        
        int ans = g.flow((sx * n + sy) * 2, n * 4 + 1);
        if (ans == INF) {
            ans = -1;
        }
        return ans;
    }
};


// 作者：zerotrac2
// 链接：https://leetcode-cn.com/problems/7rLGCR/solution/lcp-38-shou-wei-cheng-bao-by-zerotrac2-kgv2/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。