class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        typedef pair<int, int> pii;

        // 以所有小偷为起点进行多源 bfs
        short dir[4][2] = {0, 1, 1, 0, -1, 0, 0, -1};
        int dis[n][m];
        memset(dis, -1, sizeof(dis));
        queue<pii> q;
        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (grid[i][j] == 1) {
            q.push(pii(i, j));
            dis[i][j] = 0;
        }
        while (!q.empty()) {
            pii p = q.front(); q.pop();
            int i = p.first, j = p.second;
            for (int k = 0; k < 4; k++) {
                int ii = i + dir[k][0], jj = j + dir[k][1];
                if (ii < 0 || jj < 0 || ii >= n || jj >= m || dis[ii][jj] >= 0) continue;
                q.push(pii(ii, jj));
                dis[ii][jj] = dis[i][j] + 1;
            }
        }

        // 通过一次 bfs，检查能否只经过安全系数大于等于 lim 的格子，从左上角走到右下角
        auto check = [&](int lim) {
            bool vis[n][m];
            memset(vis, 0, sizeof(vis));
            queue<pii> q;
            q.push(pii(0, 0)); vis[0][0] = true;
            while (!q.empty()) {
                pii p = q.front(); q.pop();
                int i = p.first, j = p.second;
                for (int k = 0; k < 4; k++) {
                    int ii = i + dir[k][0], jj = j + dir[k][1];
                    if (ii < 0 || jj < 0 || ii >= n || jj >= m || dis[ii][jj] < lim || vis[ii][jj]) continue;
                    q.push(pii(ii, jj));
                    vis[ii][jj] = true;
                }
            }
            return vis[n - 1][m - 1];
        };

        // 二分答案
        int head = 0, tail = min(dis[0][0], dis[n - 1][m - 1]);
        while (head < tail) {
            int mid = (head + tail + 1) >> 1;
            if (check(mid)) head = mid;
            else tail = mid - 1;
        }
        return head;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/chtVBq/view/Bd2wEn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。