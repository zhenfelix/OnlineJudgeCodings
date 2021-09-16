const int inf = 0x3f3f3f3f;
const int MAXN = 100005;

struct Edge
{
    int from, to, weight, pre;
    Edge() = default;
    Edge(int f, int t, int w, int n)
        : from(f), to(t), weight(w), pre(n)
    {
    }
};

int head[MAXN];
Edge edges[MAXN * 3];
int cnt;

class Solution
{
public:
    void spfa(int s, vector<int> &dis)
    {
        int n = dis.size();
        vector<bool> inqueue(n, false);
        queue<int> q;
        q.push(s);
        inqueue[s] = true;
        dis[s] = 0;
        while (!q.empty())
        {
            int cur = q.front();
            q.pop();
            inqueue[cur] = false;
            for (int i = head[cur]; i != 0; i = edges[i].pre)
            {
                int nxt = edges[i].to;
                int w = edges[i].weight;
                if (dis[cur] + w < dis[nxt])
                {
                    dis[nxt] = dis[cur] + w;
                    if (!inqueue[nxt])
                    {
                        inqueue[nxt] = true;
                        q.push(nxt);
                    }
                }
            }
        }
    }

    void addEdge(int a, int b, int w)
    {
        edges[cnt] = Edge(a, b, w, head[a]);
        head[a] = cnt++;
    }

    int maxBuilding(int nmax, vector<vector<int>> &restrictions)
    {
        restrictions.push_back({1, 0});
        restrictions.push_back({nmax, nmax - 1});
        sort(restrictions.begin(), restrictions.end());
        int n = restrictions.size();
        cnt = 1;
        memset(head, 0, sizeof(int) * (n + 1));
        for (int i = 1; i < n; i++)
        {
            int delta = restrictions[i][0] - restrictions[i - 1][0];
            addEdge(i - 1, i, delta);
            addEdge(i, i - 1, delta);
        }

        for (int i = 0; i < n; i++)
            addEdge(n, i, restrictions[i][1]);
        vector<int> dis(n + 1, inf);
        spfa(n, dis);
        int res = 0;
        // for (auto &h : dis)
        //     cout << h << " ";
        // cout << "\n";
        for (int i = 1; i < n; i++)
        {
            int delta = restrictions[i][0] - restrictions[i - 1][0];
            res = max(res, (dis[i] + dis[i - 1] + delta) / 2);
        }
        return res;
    }
};


// const int inf = 0x3f3f3f3f;

// class Solution
// {
// public:
//     void sfpa(int s, vector<int> &dis, vector<vector<pair<int, int>>> &graph)
//     {
//         int n = dis.size();
//         vector<bool> inqueue(n, false);
//         queue<int> q;
//         q.push(s);
//         inqueue[s] = true;
//         dis[s] = 0;
//         while (!q.empty())
//         {
//             int cur = q.front();
//             q.pop();
//             inqueue[cur] = false;
//             for (auto &[nxt, w] : graph[cur])
//             {
//                 if (dis[cur] + w < dis[nxt])
//                 {
//                     dis[nxt] = dis[cur] + w;
//                     if (!inqueue[nxt])
//                     {
//                         inqueue[nxt] = true;
//                         q.push(nxt);
//                     }
//                 }
//             }
//         }
//     }

//     void addEdge(int a, int b, int w, vector<vector<pair<int, int>>> &graph)
//     {
//         graph[a].push_back({b, w});
//     }

//     int maxBuilding(int nmax, vector<vector<int>> &restrictions)
//     {
//         restrictions.push_back({1, 0});
//         restrictions.push_back({nmax, nmax-1});
//         sort(restrictions.begin(), restrictions.end());
//         int n = restrictions.size();
//         vector<vector<pair<int, int>>> graph(n+1, vector<pair<int, int>>());
//         for (int i = 1; i < n; i++)
//         {
//             int delta = restrictions[i][0] - restrictions[i - 1][0];
//             addEdge(i - 1, i, delta, graph);
//             addEdge(i, i - 1, delta, graph);
//         }
        
//         for (int i = 0; i < n; i++)
//             addEdge(n, i, restrictions[i][1], graph);
//         vector<int> dis(n+1, inf);
//         sfpa(n, dis, graph);
//         int res = 0;
//         // for (auto &h : dis)
//         //     cout << h << " ";
//         // cout << "\n";
//         for (int i = 1; i < n; i++)
//         {
//             int delta = restrictions[i][0] - restrictions[i - 1][0];
//             res = max(res, (dis[i] + dis[i - 1] + delta) / 2);
//         }
//         return res;
//     }
// };




class Solution {
public:
    int maxBuilding(int n, vector<vector<int>>& restrictions) {
        restrictions.push_back({1,0});
        restrictions.push_back({n,n});
        sort(restrictions.begin(), restrictions.end());
        int m = restrictions.size(), res = 0;
        for (int i = m-2; i >= 0; i--){
            int height = restrictions[i+1][1], position = restrictions[i+1][0];
            restrictions[i][1] = min(restrictions[i][1], position - restrictions[i][0] + height);
        }
        for (int i = 1; i < m; i++){
            int height = restrictions[i-1][1], position = restrictions[i-1][0];
            restrictions[i][1] = min(restrictions[i][1],  restrictions[i][0] - position + height);
            int h = restrictions[i][0] - position + height;
            res = max(res, h - (h - restrictions[i][1] + 1)/2);
        }
        return res;
    }
};