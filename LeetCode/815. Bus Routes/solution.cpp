const int inf = 0x3f3f3f3f;

class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target)
            return 0;
        int n = routes.size();
        unordered_map<int,vector<int>> mp;
        vector<vector<bool>> graph(n,vector<bool>(n,false));
        queue<int> q;
        vector<int> state(n,0), dist(n,0);
        for (int i = 0; i < n; i++){
            for (auto station : routes[i])
                mp[station].push_back(i);
        }
        for (auto [k, vs] : mp){
            int m = vs.size();
            for (int i = 0; i < m; i++){
                for (int j = i+1; j < m; j++){
                    graph[vs[i]][vs[j]] = true;
                    graph[vs[j]][vs[i]] = true;
                }
            }
        }
        for (auto i : mp[source]){
            state[i] |= 1;
            q.push(i);
        }
        for (auto i : mp[target]){
            state[i] |= 2;
            q.push(i);
        }
        while (!q.empty()){
            int cur = q.front(); q.pop();
            if (state[cur] == 3)
                return dist[cur]+1;
            for (int nxt = 0; nxt < n; nxt++){
                if (graph[cur][nxt] && !(state[cur] & state[nxt])){
                    state[nxt] |= state[cur];
                    dist[nxt] += dist[cur]+1;
                    q.push(nxt);
                }
            }
        }
        return -1;
    }
};



// const int maxn = 500;
// bitset<maxn> graph[500];

// class Solution {
// public:
//     int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
//         if (source == target)
//             return 0;
//         int n = routes.size();
//         unordered_map<int,vector<int>> mp;
//         queue<int> q;
//         vector<int> state(n,0), dist(n,0);
//         for (int i = 0; i < n; i++){
//             for (auto station : routes[i])
//                 mp[station].push_back(i),graph[i].reset();
//         }
//         for (auto [k, vs] : mp){
//             int m = vs.size();
//             for (int i = 0; i < m; i++){
//                 for (int j = i+1; j < m; j++){
//                     graph[vs[i]][vs[j]] = 1;
//                     graph[vs[j]][vs[i]] = 1;
//                 }
//             }
//         }
//         for (auto i : mp[source]){
//             state[i] |= 1;
//             q.push(i);
//         }
//         for (auto i : mp[target]){
//             state[i] |= 2;
//             q.push(i);
//         }
//         while (!q.empty()){
//             int cur = q.front(); q.pop();
//             if (state[cur] == 3)
//                 return dist[cur]+1;
//             for (int nxt = 0; nxt < n; nxt++){
//                 if (graph[cur][nxt] && !(state[cur] & state[nxt])){
//                     state[nxt] |= state[cur];
//                     dist[nxt] += dist[cur]+1;
//                     q.push(nxt);
//                 }
//             }
//         }
//         return -1;
//     }
// };