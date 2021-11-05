// using pii = pair<int,int>;

// class Solution {
// public:
//     int minCostToSupplyWater(int n, vector<int>& wells, vector<vector<int>>& pipes) {
//         for (int i = 0; i < n; i++){
//             pipes.push_back({0,i+1,wells[i]});
//         }
//         int m = pipes.size();
//         vector<pii> edges(m);
//         for (int i = 0; i < m; i++){
//             edges[i] = {pipes[i][2],i};
//         }
//         sort(edges.begin(), edges.end());

//         vector<int> parent(n+1);
//         for (int i = 0; i <= n; i++)
//             parent[i] = i;

//         function<int(int)> find = [&](int u){
//             if (parent[u] != u)
//                 parent[u] = find(parent[u]);
//             return parent[u];
//         };
//         auto merge = [&](int u, int v){
//             int ru = find(u), rv = find(v);
//             if (ru != rv){
//                 parent[ru] = rv;
//                 return true;
//             }
//             return false;
//         };

//         int ans = 0, cnt = 0;
//         for (auto [c,i] : edges){
//             int u = pipes[i][0], v = pipes[i][1];
//             if (merge(u,v)){
//                 ans += c;
//                 cnt++;
//                 if (cnt == n)
//                     break;
//             }
//         }
//         return ans;
//     }
// };













using pii = pair<int,int>;

class Solution {
public:
    int minCostToSupplyWater(int n, vector<int>& wells, vector<vector<int>>& edges) {
        for (int i = 0; i < n; i++){
            edges.push_back({0,i+1,wells[i]});
        }
        int m = edges.size();
        vector<vector<int>> graph(n+1);
        priority_queue<pii, vector<pii>, greater<pii>> pq;
        vector<bool> visited(n+1,false);
        for (int i = 0; i < m; i++){
            int u = edges[i][0], v = edges[i][1];
            graph[u].push_back(i);
            graph[v].push_back(i);
        }
        visited[0] = true;
        for (auto j : graph[0])
            pq.push({edges[j][2],j});
        int ans = 0, cnt = 0;
        while (!pq.empty() && cnt < n){
            auto [c,j] = pq.top(); pq.pop();
            int u = edges[j][0], v = edges[j][1];
            if (visited[u] && visited[v])
                continue;
            ans += c; cnt++;
            cout << c << " " << j << " " << u << " " << v << endl;
            if (!visited[v])
                u = v;
            visited[u] = true;
            for (auto j : graph[u]){
                int u = edges[j][0], v = edges[j][1];
                if (visited[u] && visited[v])
                    continue;
                pq.push({edges[j][2],j});
            }
        }

        
        return ans;
    }
};