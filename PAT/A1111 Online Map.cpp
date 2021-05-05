#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");

const int inf = 0x3f3f3f3f;
using DIS = pair<int,int>;

struct Edge
{
    int from, to, cost1, cost2;
    Edge() = default;
    Edge(int f, int t, int c1, int c2)
        : from(f), to(t), cost1(c1), cost2(c2)
        {}
};


int dijkstra(int start, int aim, map<int,vector<Edge>> &graph, vector<int> &parent){
    int n = parent.size();
    vector<DIS> dis(n, {inf,inf});
    priority_queue<pair<DIS, int>, vector<pair<DIS, int>>, greater<pair<DIS, int>>> pq;
    dis[start] = {0,0};
    pq.push({{0,0},start});
    while (!pq.empty())
    {
        auto item = pq.top();pq.pop();
        auto pdis = item.first;
        auto cur = item.second;
        if (dis[cur] < pdis)
            continue;
        if (cur == aim)
            break;
        for (auto edge : graph[cur]){
            auto nxt = edge.to;
            auto cost1 = edge.cost1;
            auto cost2 = edge.cost2;
            DIS tmp = {pdis.first+cost1, pdis.second+cost2};
            if (tmp < dis[nxt]){
                dis[nxt] = tmp;
                pq.push({tmp,nxt});
                parent[nxt] = cur;
            }
        }
    }
    return dis[aim].first;
}



class Solution
{
public:
    void decode()
    {
        
    }
};



int main()
{
    // ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
    // freopen("input", "r", stdin);

    
    Solution sol;
    int n, m, start, aim;
    cin >> n >> m;
    vector<int> parent_d(n), parent_t(n);
    map<int, vector<Edge>> graph_d, graph_t;
    int from, to, one_way, len, time;
    while(m--){
        cin >> from >> to >> one_way >> len >> time;
        graph_d[from].push_back(Edge(from, to, len, time));
        graph_t[from].push_back(Edge(from, to, time, 1));
        if (one_way == 0){
            graph_d[to].push_back(Edge(to, from, len, time));
            graph_t[to].push_back(Edge(to, from, time, 1));
        }
    }
    cin >> start >> aim;
    int cost_d = dijkstra(start, aim, graph_d, parent_d);
    int cost_t = dijkstra(start, aim, graph_t, parent_t);
    bool same = true;
    vector<int> path_d, path_t;
    for (int cur_d = aim, cur_t = aim; cur_d != start || cur_t != start;){
        if (cur_d != cur_t){
            same = false;
        }
        if (cur_d != start){
            path_d.push_back(cur_d);
            cur_d = parent_d[cur_d];
        }
        if (cur_t != start){
            path_t.push_back(cur_t);
            cur_t = parent_t[cur_t];
        }
    }
    path_d.push_back(start);
    path_t.push_back(start);
    
    if (same){
        cout << "Distance = " << cost_d << "; Time = " << cost_t << ": ";
        for(auto it = path_d.rbegin(); it != path_d.rend(); it++){
            cout << *it;
            if (*it != aim){
                cout << " -> ";
            }
        }
        cout << endl;
    }
    else{
        cout << "Distance = " << cost_d << ": ";
        for (auto it = path_d.rbegin(); it != path_d.rend(); it++)
        {
            cout << *it;
            if (*it != aim)
            {
                cout << " -> ";
            }
        }
        cout << endl;
        cout << "Time = " << cost_t << ": ";
        for (auto it = path_t.rbegin(); it != path_t.rend(); it++)
        {
            cout << *it;
            if (*it != aim)
            {
                cout << " -> ";
            }
        }
        cout << endl;
    }
}