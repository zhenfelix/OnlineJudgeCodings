class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        int n = servers.size(), m = tasks.size();
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> available, todo;
        int cur = 0, clock = 0;
        vector<int> ans(m);
        for (int i = 0; i < n; i++){
            available.push({servers[i],i});
        }
        while (cur < m){
            while (!todo.empty() && todo.top().first == clock){
                auto [t,idx] = todo.top();todo.pop();
                available.push({servers[idx],idx});
            }
            while (cur <= min(clock, m-1) && !available.empty()){
                auto [w, idx] = available.top();available.pop();
                todo.push({clock+tasks[cur],idx});
                ans[cur++] = idx;
            }
            clock = clock < m ? clock+1 : todo.top().first;
        }
        return ans;
    }
};