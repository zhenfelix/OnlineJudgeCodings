class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        vector<bool> known(n);
        known[0] = true;
        known[firstPerson] = true;
  
        int maxT = 0;
        for (auto &meeting : meetings)
            maxT = max(maxT, meeting[2]);
        vector<vector<pair<int, int>>> time(maxT + 1);
        for (auto &meeting : meetings)
            time[meeting[2]].emplace_back(meeting[0], meeting[1]);
        
        vector<vector<int>> adj(n); // 复用邻接表
        for (int i = 1; i <= maxT; ++i) {
            if (time[i].empty())
                continue;
            
            queue<int> q;
            unordered_set<int> vis; // 用集合，而不是布尔数组
            for (auto &[u, v] : time[i]) { // 设置邻接表
                adj[u].emplace_back(v);
                adj[v].emplace_back(u);
                if (known[u] && !vis.count(u)) {
                    q.push(u);
                    vis.insert(u);
                }
                if (known[v] && !vis.count(v)) {
                    q.push(v);
                    vis.insert(v);
                }
            }
            
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : adj[u]) {
                    if (!known[v]) {
                        known[v] = true;
                        q.push(v);
                    }
                }
            }
            
            for (auto &[u, v] : time[i]) { // 还原邻接表
                adj[u].clear();
                adj[v].clear();
            }
        }
        
        vector<int> ans;
        for (int i = 0; i < n; ++i)
            if (known[i])
                ans.push_back(i);
        return ans;
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/S0NvzF/view/w3E3WF/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        vector<bool> known(n);
        known[0] = true;
        known[firstPerson] = true;
  
        int maxT = 0;
        for (auto &meeting : meetings)
            maxT = max(maxT, meeting[2]);
        vector<vector<pair<int, int>>> time(maxT + 1);
        for (auto &meeting : meetings)
            time[meeting[2]].emplace_back(meeting[0], meeting[1]);
        
        vector<vector<int>> adj(n); // 复用邻接表
        for (int i = 1; i <= maxT; ++i) {
            if (time[i].empty())
                continue;
            
            unordered_set<int> vis; // 用集合，而不是布尔数组
            queue<int> q;
            for (auto &[u, v] : time[i]) { // 设置邻接表
                adj[u].emplace_back(v);
                adj[v].emplace_back(u);
                if (known[u] && !vis.count(u)) {
                    vis.insert(u);
                    q.push(u);
                }
                if (known[v] && !vis.count(v)) {
                    vis.insert(v);
                    q.push(v);
                }
            }
            
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : adj[u]) {
                    if (!vis.count(v)) {
                        known[v] = true;
                        vis.insert(v);
                        q.push(v);
                    }
                }
            }
            
            for (auto &[u, v] : time[i]) { // 还原邻接表
                adj[u].clear();
                adj[v].clear();
            }
        }
        
        vector<int> ans;
        for (int i = 0; i < n; ++i)
            if (known[i])
                ans.push_back(i);
        return ans;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/S0NvzF/view/w3E3WF/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        vector<bool> known(n);
        known[0] = true;
        known[firstPerson] = true;
  
        int maxT = 0;
        for (auto &meeting : meetings)
            maxT = max(maxT, meeting[2]);
        vector<vector<pair<int, int>>> time(maxT + 1);
        for (auto &meeting : meetings)
            time[meeting[2]].emplace_back(meeting[0], meeting[1]);
        
        
        for (int i = 1; i <= maxT; ++i) {
            if (time[i].empty())
                continue;
            unordered_map<int, vector<int>> adj; // 复用邻接表
            unordered_set<int> vis; // 用集合，而不是布尔数组
            queue<int> q;
            for (auto &[u, v] : time[i]) { // 设置邻接表
                adj[u].emplace_back(v);
                adj[v].emplace_back(u);
                if (known[u] && !vis.count(u)) {
                    vis.insert(u);
                    q.push(u);
                }
                if (known[v] && !vis.count(v)) {
                    vis.insert(v);
                    q.push(v);
                }
            }
            
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : adj[u]) {
                    if (!vis.count(v)) {
                        known[v] = true;
                        vis.insert(v);
                        q.push(v);
                    }
                }
            }
            
        }
        
        vector<int> ans;
        for (int i = 0; i < n; ++i)
            if (known[i])
                ans.push_back(i);
        return ans;
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/S0NvzF/view/w3E3WF/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。