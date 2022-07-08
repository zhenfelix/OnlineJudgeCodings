using PII = pair<int,int>;
const int N = 1e5 + 7;
int ind[N];
class Solution {
public:
    vector<int> distanceToCycle(int n, vector<vector<int>>& edges) {
        // 拓扑排序
        vector<int> res(n,0);
        memset(ind,0,4 * n);
        vector<vector<int>> g(n);
        for(auto& e : edges) {
            ind[e[0]] ++ , ind[e[1]] ++;
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        queue<int> q;
        for(int i = 0;i < n;i ++) if(ind[i] == 1) q.push(i) , ind[i] --;
        while(!q.empty()) {
            auto t = q.front(); q.pop();
            for(auto& next : g[t]) {
                if(ind[next]) ind[next] --;
                if(ind[next] == 1) {
                    ind[next] --;
                    q.push(next);
                }
            }
        }
        // 然后再跑一遍
        for(int i = 0;i < n;i ++) if(ind[i]) q.push(i);
        while(!q.empty()) {
            auto t = q.front(); q.pop();
            for(auto& next : g[t]) {
                if(!ind[next]) {
                    ind[next] ++;
                    res[next] = res[t] + 1;
                    q.push(next);
                }
            }
        }
        return res;
    }
};


// 作者：daydayUppp
// 链接：https://leetcode.cn/problems/distance-to-a-cycle-in-undirected-graph/solution/daydayupppqiqiu-by-daydayuppp-bzvr/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。