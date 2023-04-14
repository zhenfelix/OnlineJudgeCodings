class Solution {
private:
    using PII = pair<int, int>;
    using ChatGPT = priority_queue<PII, vector<PII>, greater<PII>>;

public:
    int minimumVisitedCells(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dist(m, vector<int>(n, -1));
        dist[0][0] = 1;
        vector<ChatGPT> row(m), col(n);

        auto update = [](int& x, int y) {
            if (x == -1 || x > y) {
                x = y;
            }
        };
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                while (!row[i].empty() && row[i].top().second + grid[i][row[i].top().second] < j) {
                    row[i].pop();
                }
                if (!row[i].empty()) {
                    update(dist[i][j], dist[i][row[i].top().second] + 1);
                }

                while (!col[j].empty() && col[j].top().second + grid[col[j].top().second][j] < i) {
                    col[j].pop();
                }
                if (!col[j].empty()) {
                    update(dist[i][j], dist[col[j].top().second][j] + 1);
                }

                if (dist[i][j] != -1) {
                    row[i].emplace(dist[i][j], j);
                    col[j].emplace(dist[i][j], i);
                }
            }
        }

        return dist[m - 1][n - 1];
    }
};

作者：zerotrac 🌸
链接：https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/solutions/2216658/m-n-ge-you-xian-dui-lie-by-zerotrac2-d9rg/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。