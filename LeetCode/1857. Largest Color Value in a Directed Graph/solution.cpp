// class Solution {
// public:
//     int largestPathValue(string colors, vector<vector<int>>& edges) {
//         int n = colors.size();
//         vector<vector<int>> dp(n, vector<int>(26,0));
//         vector<int> indegree(n,0);
//         vector<vector<int>> graph(n, vector<int>());
//         queue<int> q;
//         int res = 0, visited = 0;
//         for (auto &e : edges){
//             graph[e[0]].push_back(e[1]);
//             indegree[e[1]]++;
//         }
//         for (int i = 0; i < n; i++){
//             if (indegree[i] == 0){
//                 dp[i][colors[i]-'a']++;
//                 q.push(i);
//                 visited++;
//                 res = 1;
//             }
                
//         }
//         while (!q.empty()){
//             int cur = q.front(); q.pop();
//             for (auto nxt : graph[cur]){
//                 for (int i = 0; i < 26; i++){
//                     dp[nxt][i] = max(dp[nxt][i], (colors[nxt]-'a' == i ? 1 : 0)+dp[cur][i]);
//                     res = max(res, dp[nxt][i]);
//                 }
//                 indegree[nxt]--;
//                 if (indegree[nxt] == 0){
//                     q.push(nxt);
//                     visited++;
//                 }
//             }
//         }
//         if (visited == n){
//             return res;
//         }
//         return -1;
        
//     }
// };

// class Solution {
// public:
//     int largestPathValue(string colors, vector<vector<int>>& edges) {
//         int n = colors.size();
//         // vector<vector<int>> dp(n, vector<int>(26,0));
//         vector<vector<int>> graph(n, vector<int>());
//         vector<int> indegree_orgin(n,0);
//         int res = 0;
//         for (auto &e : edges){
//             graph[e[0]].push_back(e[1]);
//             indegree_orgin[e[1]]++;
//         }
//         for (int c = 0; c < 26; c++){
//             vector<int> dp(n,0);
//             int visited = 0;
//             queue<int> q;
//             vector<int> indegree = indegree_orgin;
//             for (int i = 0; i < n; i++){
//                 if (indegree[i] == 0){
//                     if (colors[i] == 'a'+c)
//                         res = max(res, ++dp[i]);
//                     q.push(i);
//                     visited++;
//                 }
                    
//             }
//             while (!q.empty()){
//                 int cur = q.front(); q.pop();
//                 for (auto nxt : graph[cur]){
//                     dp[nxt] = max(dp[nxt], dp[cur]+(colors[nxt] == 'a'+c ? 1 : 0));
//                     res = max(res, dp[nxt]);
//                     indegree[nxt]--;
//                     if (indegree[nxt] == 0){
//                         q.push(nxt);
//                         visited++;
//                     }
//                 }
//             }
//             // cout << visited << endl;
//             if (visited != n)
//                 return -1;
//         }
//         return res;
//     }
// };


class Solution {
public:
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        int n = colors.size();
        vector<int> deg(n);
        vector<vector<int>> adj(n);
        for (auto &edge : edges) {
            int u = edge[0], v = edge[1];
            deg[v]++;
            adj[u].emplace_back(v);
        }
        
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (deg[i] == 0)
                q.push(i);
        }
        
        vector<int> topo;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            topo.emplace_back(u);
            for (int v : adj[u]) {
                deg[v]--;
                if (deg[v] == 0)
                    q.push(v);
            }
        }
        
        if (topo.size() != n)
            return -1;
        
        int ans = 0;
        for (int color = 0; color < 26; ++color) {
            vector<int> dp(n);
            for (int i = n - 1; i >= 0; --i) {
                int u = topo[i];
                for (int v : adj[u])
                    dp[u] = max(dp[u], dp[v]);
                if (colors[u] - 'a' == color)
                    dp[u]++;
                ans = max(ans, dp[u]);
            }
        }
        
        return ans;
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/7QlTIV/view/2CLPG9/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution {
public:
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        int n = colors.length(), res = 0;
        vector<vector<int>> dp(n, vector<int>(26,0)), graph(n);
        for (int i = 0; i < n; i++){
            dp[i][colors[i]-'a']++;
        }
        vector<int> degree(n,0), q;
        for (auto edge : edges){
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            degree[v]++;
        }
        int cnt = 0;
        for (int i = 0; i < n; i++)
            if (degree[i] == 0){
                q.push_back(i);
                cnt++;
            }
        while (!q.empty()){
            int cur = q.back();q.pop_back();
            for (int i = 0; i < 26; i++)
                res = max(res, dp[cur][i]);
            for (auto nxt : graph[cur]){
                for (int i = 0; i < 26; i++){
                    dp[nxt][i] = max(dp[nxt][i], dp[cur][i]+(colors[nxt]-'a'==i));
                }
                degree[nxt]--;
                if (degree[nxt] == 0){
                    q.push_back(nxt);
                    cnt++;
                }
            }
        }
        return cnt < n ? -1 : res;

    }
};