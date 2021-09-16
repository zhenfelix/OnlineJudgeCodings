// class Solution {
// public:
//     int minTrioDegree(int n, vector<vector<int>>& edges) {
//         vector<unordered_set<int>> graph(n);
//         int res = INT_MAX;
//         for (auto e : edges){
//             graph[e[0]-1].insert(e[1]-1);
//             graph[e[1]-1].insert(e[0]-1);
//         }
//         for (int i = 0; i < n; i++){
//             for (auto j : graph[i]){
//                 for (auto k : graph[j])
//                     if (graph[i].find(k) != graph[i].end()){
//                         int len = graph[i].size();
//                         len += graph[j].size();
//                         len += graph[k].size();
//                         res = min(res, len-6);
//                     }
//             }
//         }
//         return res == INT_MAX ? -1 : res;
//     }
// };

class Solution {
public:
    int minTrioDegree(int n, vector<vector<int>>& edges) {
        vector<unordered_set<int>> d(n);
        for (auto &e : edges) {
            int u = e[0] - 1, v = e[1] - 1;
            d[u].insert(v), d[v].insert(u);
        }
        
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            int u = e[0] - 1, v = e[1] - 1;
            if (d[u].size() < d[v].size() || (d[u].size() == d[v].size() && u < v))
                adj[u].emplace_back(v);
            else
                adj[v].emplace_back(u);
        }

        int ans = INT_MAX;
        for (int u = 0; u < n; ++u)
            for (int v : adj[u])
                for (int w : adj[v])
                    if (d[u].count(w))
                        ans = min(ans, (int)(d[u].size() + d[v].size() + d[w].size() - 6));
        
        return ans == INT_MAX ? -1 : ans;
    }
};


// 作者：lucifer1004
// 链接：https://leetcode-cn.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/solution/gei-wu-xiang-tu-ding-xiang-by-lucifer100-c72d/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    int minTrioDegree(int n, vector<vector<int>>& edges) {
    int i, ans = INT_MAX;
    vector<int> C(n);
    vector<bitset<400>> A(n);

    for(auto &e: edges){
        e[0]--, e[1]--;
        A[e[0]].set(e[1]);
        A[e[1]].set(e[0]);
        C[e[0]]++, C[e[1]]++;
    } 
    bitset<400> bs;
    for(auto &e: edges){
        bs = A[e[0]] & A[e[1]];
        for(i = 0; i < n; i++){
            if(bs[i]) ans = min(ans, C[e[0]] + C[e[1]] + C[i] - 6);
        }
    }
    return (ans == INT_MAX ? -1 : ans);
}
};

