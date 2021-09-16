class Solution
{
public:
    vector<int> countSubgraphsForEachDiameter(int n, vector<vector<int>> &edges)
    {
        vector<vector<int>> dist(n, vector<int>(n, n));
        unordered_map<int, int> mp;
        vector<int> graph(n, 0);
        for (int i = 0; i < n; i++)
        {
            dist[i][i] = 0;
            mp[1 << i] = i;
        }
        for (auto e : edges)
        {
            dist[e[0] - 1][e[1] - 1] = 1;
            dist[e[1] - 1][e[0] - 1] = 1;
            graph[e[0] - 1] |= (1 << (e[1] - 1));
            graph[e[1] - 1] |= (1 << (e[0] - 1));
        }
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
        vector<int> cnt(n - 1, 0), dp(1 << n, -1);
        for (int i = 0; i < n; i++)
            dp[1 << i] = 0;
        for (int s = 1; s < (1 << n); s++)
        {
            for (int i = 0; i < n; i++)
            {
                if (((s >> i) & 1) && dp[s ^ (1 << i)] != -1 && (graph[i] & (s ^ (1 << i))))
                {
                    int t = s ^ (1 << i);
                    dp[s] = dp[t];
                    for (int j = 0; j < n; j++)
                    {
                        if ((t >> j) & 1)
                        {
                            dp[s] = max(dp[s], dist[i][j]);
                        }
                    }
                    if (dp[s])
                    {
                        cnt[dp[s] - 1]++;
                    //     cout << s << " " << dp[s] << endl;
                    }
                    break;
                }
            }
        }
        return cnt;
    }
};