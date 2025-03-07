class Solution {
public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();

        const int INF = 1e9;
        int f[n][m][2];
        // dir[k + 1] 是 dir[k] 的顺时针方向
        short dir[4][2] = {1, 1, 1, -1, -1, -1, -1, 1};
        // k 表示当前 dp 在转弯前是什么方向
        int k;

        // 检查 (i, j) 能否从 (ii, jj) 走过来
        auto check = [&](int i, int j, int ii, int jj) {
            if (ii < 0 || jj < 0 || ii >= n || jj >= m) return false;
            int x = grid[i][j], y = grid[ii][jj];
            // 2 的上一个可以是 1 和 0
            if (x == 2) return y != 2;
            // 0 的上一个只能是 2
            else return y == 2;
        };

        // 记忆化搜索
        auto dp = [&](this auto &&self, int i, int j, int t) {
            if (grid[i][j] == 1) return 1;
            int &ret = f[i][j][t];
            if (ret > -INF) return ret;
            ret = -INF + 1;

            if (t == 0) {
                // 还没转弯前的上一个方向
                int ii = i - dir[k][0], jj = j - dir[k][1];
                if (check(i, j, ii, jj)) ret = max(ret, self(ii, jj, 0) + 1);
            } else {
                // 转弯后的上一个方向
                int ii = i - dir[(k + 1) % 4][0], jj = j - dir[(k + 1) % 4][1];
                if (check(i, j, ii, jj)) ret = max({ret, self(ii, jj, 0) + 1, self(ii, jj, 1) + 1});
            }
            return ret;
        };

        int ans = 0;
        // 枚举 dp 的方向
        for (k = 0; k < 4; k++) {
            for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) f[i][j][0] = f[i][j][1] = -INF;
            for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) ans = max({ans, dp(i, j, 0), dp(i, j, 1)});
        }
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/SoR3j0/view/pgyMOB/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。