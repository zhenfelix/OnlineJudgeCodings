class Solution {
public:
    int findShortestCycle(int n, vector<vector<int>>& edges) {
        int res = n + 1;
        vector<int> nes[n];
        for(const auto& e : edges)
            nes[e[0]].push_back(e[1]), nes[e[1]].push_back(e[0]);
        for(const auto& e : edges) {
                // 枚举边 (u=i, v=nes[i][j])。由于边数不超过 1000，故不会超时
                int u = e[0], v = e[1];
                queue<int> q({u});
                vector<int> dis(n, n + 1);
                dis[u] = 0;
                while(q.size()) {
                    int cur = q.front();
                    q.pop();
                    for(int ne : nes[cur]) {
                        if(!(cur == u && ne == v) && dis[ne] == n+1) {
                            dis[ne] = dis[cur] + 1;
                            q.push(ne);
                        }
                    }
                }
                res = min(res, 1 + dis[v]);
            }
        return res > n? -1 : res;
    }
};



class Solution {
public:
    int findShortestCycle(int n, vector<vector<int>>& edges) {
        int res = n + 1;
        vector<int> nes[n];
        for(const auto& e : edges)
            nes[e[0]].push_back(e[1]), nes[e[1]].push_back(e[0]);
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < nes[i].size(); ++j) {
                // 枚举边 (u=i, v=nes[i][j])。由于边数不超过 1000，故不会超时
                queue<int> q({i});
                vector<int> dis(n, n + 1);
                dis[i] = 0;
                while(q.size()) {
                    int cur = q.front();
                    q.pop();
                    for(int ne : nes[cur]) {
                        if(!(cur == i && ne == nes[i][j]) && dis[ne] == n+1) {
                            dis[ne] = dis[cur] + 1;
                            q.push(ne);
                        }
                    }
                }
                res = min(res, 1 + dis[nes[i][j]]);
            }
        }
        return res > n? -1 : res;
    }
};


作者：newhar
链接：https://leetcode.cn/problems/shortest-cycle-in-a-graph/solutions/2203454/liang-chong-zuo-fa-shan-bian-huo-mei-ju-z4t8s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。