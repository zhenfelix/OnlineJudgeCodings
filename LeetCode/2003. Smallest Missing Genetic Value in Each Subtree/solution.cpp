class Solution
{
public:
    vector<int> smallestMissingValueSubtree(vector<int> &parents, vector<int> &nums)
    {
        int n = parents.size();
        vector<vector<int>> graph(n);
        unordered_map<int, int> mp;
        for (int i = 0; i < n; i++)
            if (parents[i] != -1)
                graph[parents[i]].push_back(i);
        for (int i = 0; i < n; i++)
            mp[nums[i]] = i;

        vector<int> ans(n, 1), tin(n, 0), tout(n, 0);
        vector<bool> visited(n, false);
        int clock = 1;

        function<int(int)> dfs = [&](int cur)
        {
            tin[cur] = clock++;
            int mi = 1;
            for (auto nxt : graph[cur])
            {
                mi = max(mi, dfs(nxt));
            }
            visited[cur] = true;
            tout[cur] = clock++;
            while (mp.find(mi) != mp.end() && visited[mp[mi]] && tin[mp[mi]] >= tin[cur] && tout[mp[mi]] <= tout[cur])
                mi++;
            ans[cur] = mi;
            return mi;
        };
        dfs(0);
        return ans;
    }
};



作者：ga-beng-cui-7
链接：https://leetcode-cn.com/problems/smallest-missing-genetic-value-in-each-subtree/solution/hou-xu-bian-li-ji-lu-jin-ru-he-chu-qu-de-b01y/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。