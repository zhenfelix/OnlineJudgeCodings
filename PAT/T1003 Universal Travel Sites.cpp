#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

struct Edge
{
    int from, to, cost, nxt;
    Edge(int f, int t, int c, int n)
        : from(f), to(t), cost(c), nxt(n)
        {}
};

void addEdge(int a, int b, int cost, vector<Edge> &edges, vector<int> &head){
    int nxt = head[a];
    head[a] = edges.size();
    edges.push_back(Edge(a,b,cost,nxt));
}

int bfs(int start, int aim, vector<Edge> &edges, vector<int> &head, vector<int> &parent){
    int nv = head.size();
    parent.assign(nv,-1);
    queue<pair<int,int>> q;
    vector<bool> visited(nv, false);
    q.push({start,inf});
    visited[start] = true;
    while (!q.empty())
    {
        auto item = q.front(); q.pop();
        int cur = item.first, delta = item.second;
        if (cur == aim)
            return delta;
        for (int i = head[cur]; i != -1; i = edges[i].nxt){
            if (!visited[edges[i].to] && edges[i].cost > 0){
                visited[edges[i].to] = true;
                q.push({edges[i].to, min(delta,edges[i].cost)});
                parent[edges[i].to] = i;
            }
        }

    }
    return 0;
    
}

int maxflow(int start, int aim, vector<Edge> &edges, vector<int> &head){
    int flow = 0;
    vector<int> parent;
    while (int delta = bfs(start,aim,edges,head,parent)){
        for (int cur = aim; cur != start; cur = edges[parent[cur]].from)
        {
            edges[parent[cur]].cost -= delta;
            edges[parent[cur]^1].cost += delta;
        }
        flow += delta;
    }
    return flow;
}


int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
//     freopen("input", "r", stdin);
    int cnt = 0, cost, n;
    string start, aim, a, b;
    cin >> start >> aim >> n;

    map<string,int> mp;
    vector<Edge> edges;
    vector<int> head(2*n+2,-1);
    mp[start] = cnt++;
    mp[aim] = cnt++;

    while (n--)
    {
        cin >> a >> b >> cost;
        if (mp.find(a) == mp.end())
            mp[a] = cnt++;
        if (mp.find(b) == mp.end())
            mp[b] = cnt++;
        addEdge(mp[a], mp[b], cost, edges, head);
        addEdge(mp[b], mp[a], 0, edges, head);
    }
    int res = maxflow(0, 1, edges, head);
    cout << res << endl;
    
    

    return 0;
}
