const int maxn = 205;
bitset<maxn> dp1[maxn], dp2[maxn];
vector<pair<int, int>> dxy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

class Solution
{
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>> &heights)
    {
        int n = heights.size(), m = heights[0].size();
        vector<vector<int>> ans;
        queue<pair<int, int>> q;
        auto bfs = [&](bitset<maxn> dp[])
        {
            while (!q.empty())
            {
                auto [r, c] = q.front();
                q.pop();
                for (auto [dx, dy] : dxy)
                {
                    dx += r;
                    dy += c;
                    if (dx >= 0 && dx < n && dy >= 0 && dy < m && !dp[dx][dy] && heights[dx][dy] >= heights[r][c])
                    {
                        q.push({dx, dy});
                        dp[dx][dy] = 1;
                    }
                }
            }
        };
        for (int i = 0; i < n; i++)
        {
            dp1[i].reset();
            q.push({i, 0});
            dp1[i][0] = 1;
        }
        for (int j = 1; j < m; j++)
        {
            q.push({0, j});
            dp1[0][j] = 1;
        }
        bfs(dp1);
        for (int i = 0; i < n; i++)
        {
            dp2[i].reset();
            q.push({i, m - 1});
            dp2[i][m - 1] = 1;
        }
        for (int j = 0; j < m - 1; j++)
        {
            q.push({n - 1, j});
            dp2[n - 1][j] = 1;
        }
        bfs(dp2);
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (dp1[i][j] && dp2[i][j])
                    ans.push_back({i, j});
            }
        }
        return ans;
    }
};