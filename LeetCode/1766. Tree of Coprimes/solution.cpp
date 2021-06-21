class Solution {
public:
    int gcd(int a, int b){
        if (b == 0)
            return a;
        return gcd(b, a%b);
    }

    void dfs(int cur, int parent, vector<int> &ans, vector<int>& nums, vector<vector<int>> &graph, vector<vector<pair<int,int>>> &path, int level){
        int depth = -1;
        for (int i = 1; i <= 50; i++){
            if (!path[i].empty() && path[i].back().second > depth && gcd(i, nums[cur]) == 1){
                depth = path[i].back().second;
                ans[cur] = path[i].back().first;
            }
        }
        path[nums[cur]].push_back({cur,level});
        for (auto nxt : graph[cur]){
            if (nxt == parent)
                continue;
            dfs(nxt, cur, ans, nums, graph, path, level+1);
        }
        path[nums[cur]].pop_back();
    }

    vector<int> getCoprimes(vector<int>& nums, vector<vector<int>>& edges) {
        int n = nums.size();
        vector<vector<int>> graph(n);
        vector<int> ans(n, -1);
        for (auto edge : edges){
            int a = edge[0], b = edge[1];
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        vector<vector<pair<int,int>>> path(55);
        dfs(0, -1, ans, nums, graph, path, 0);
        return ans;

    }
};