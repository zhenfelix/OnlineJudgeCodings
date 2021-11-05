class Solution {
public:
    int minimumSemesters(int n, vector<vector<int>>& relations) {
        vector<vector<int>> graph(n+1);
        vector<int> indegree(n+1);
        for (auto relation : relations){
            graph[relation[0]].push_back(relation[1]);
            indegree[relation[1]]++;
        }
        queue<int> q;
        int step = 0, cnt = 0;
        for (int i = 1; i <= n; i++)
            if (indegree[i] == 0)
                q.push(i);
        while (!q.empty()){
            int len = q.size();
            for (int j = 0; j < len; j++){
                auto cur = q.front(); q.pop();
                cnt++;
                for (auto nxt : graph[cur]){
                    indegree[nxt]--;
                    if (indegree[nxt] == 0)
                        q.push(nxt);
                }
            }
            step++;
        }
        if (cnt < n)
            return -1;
        return step;
    }
};