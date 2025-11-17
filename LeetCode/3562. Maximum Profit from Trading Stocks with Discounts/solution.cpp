class Solution {
public:
    vector<vector<int>> g;
    vector<int> parent;

    vector<vector<vector<int>>> memo1;
    vector<vector<vector<int>>> memo2;

    int dfs1(int cur, int flag, int b, const vector<int>& present, const vector<int>& future) {
        if (memo1[cur][flag][b] != -1) {
            return memo1[cur][flag][b];
        }
        int cost = (flag == 1) ? (present[cur] / 2) : present[cur];
        int ans = dfs2(cur, 0, 0, b, present, future);
        if (cost <= b) {
            ans = max(ans, dfs2(cur, 0, 1, b - cost, present, future) + future[cur] - cost);
        }
        return memo1[cur][flag][b] = ans;
    }

    int dfs2(int pre, int i, int flag, int b, const vector<int>& present, const vector<int>& future) {
        
        int m = g[pre].size();
        if (i == m) {
            return 0;
        }
        int cur = g[pre][i];
        if (memo2[cur][flag][b] != -1) {
            return memo2[cur][flag][b];
        }
        int ans = 0;
        for (int nb = 0; nb <= b; ++nb) {
            ans = max(ans, dfs1(cur, flag, nb, present, future) + dfs2(pre, i + 1, flag, b - nb, present, future));
        }
        return memo2[cur][flag][b] = ans;
    }

    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        g.resize(n);
        parent.resize(n);

        for (const auto& edge : hierarchy) {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            g[u].push_back(v);
            parent[v] = u;
        }

        memo1.assign(n, vector<vector<int>>(2, vector<int>(budget + 1, -1)));
        memo2.assign(n, vector<vector<int>>(2, vector<int>(budget + 1, -1)));

        int res = dfs1(0, 0, budget, present, future);

        return res;
    }
};