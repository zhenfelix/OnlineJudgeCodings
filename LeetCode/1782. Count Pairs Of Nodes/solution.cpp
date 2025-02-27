class Solution {
public:
vector<int> countPairs(int n, vector<vector<int>>& edges, vector<int>& queries) {
    vector<int> cnt(n + 1), sorted_cnt(n + 1), res;
    vector<unordered_map<int, int>> shared(n + 1);
    for (auto &e : edges) {
        sorted_cnt[e[0]] = cnt[e[0]] = cnt[e[0]] + 1;
        sorted_cnt[e[1]] = cnt[e[1]] = cnt[e[1]] + 1;
        ++shared[min(e[0], e[1])][max(e[0], e[1])];
    }
    sort(begin(sorted_cnt), end(sorted_cnt));
    for (auto &q : queries) {
        res.push_back(0);
        for (int i = 1, j = n; i < j; )
            if (q < sorted_cnt[i] + sorted_cnt[j])
                res.back() += (j--) - i;
            else
                ++i;
        for (auto i = 1; i <= n; ++i)
            for (auto [j, sh_cnt]: shared[i])
                if (q < cnt[i] + cnt[j] && q + sh_cnt >= cnt[i] + cnt[j])
                    --res.back();
    }
    return res;
}
};


class Solution
{
public:
    vector<int> countPairs(int n, vector<vector<int>> &edges, vector<int> &queries)
    {
        vector<int> degree(n), idx(n), ans;
        vector<map<int, int>> graph(n);
        for (int i = 0; i < n; i++)
            idx[i] = i;
        for (auto e : edges)
        {
            degree[e[0]-1]++;
            degree[e[1]-1]++;
            graph[e[0]-1][e[1]-1]++;
            graph[e[1]-1][e[0]-1]++;
        }
        sort(idx.begin(), idx.end(), [&](int a, int b)
             { return degree[a] < degree[b]; });
        for (auto q : queries)
        {
            int res = 0, right = n - 1;
            vector<bool> seen(n, false);
            for (int left = 0; left < n; left++)
            {
                while (left < right && degree[idx[left]] + degree[idx[right]] > q)
                {
                    seen[idx[right]] = true;
                    right--;
                }
                if (left > right)
                {
                    right++;
                    seen[idx[right]] = false;
                }
                res += n - 1 - right;

                    for (auto [k, v] : graph[idx[left]])
                    {
                        if (degree[idx[left]] + degree[k] - v <= q && seen[k])
                            res--;
                    }
            }
            ans.push_back(res);
        }
        return ans;
    }
};