class Solution {
public:
    int countUnguarded(int n, int m, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<bool>> G, W, f;
        G.resize(n, vector<bool>(m));
        W.resize(n, vector<bool>(m));
        f.resize(n, vector<bool>(m));
        for (auto &g : guards) G[g[0]][g[1]] = true;
        for (auto &w : walls) W[w[0]][w[1]] = true;

        #define GAO { \
            if (G[i][j]) now = true; \
            else if (W[i][j]) now = false; \
            if (now) f[i][j] = true; \
        }

        for (int i = 0; i < n; i++) {
            bool now = false;
            for (int j = 0; j < m; j++) GAO
            now = false;
            for (int j = m - 1; j >= 0; j--) GAO
        }
        for (int j = 0; j < m; j++) {
            bool now = false;
            for (int i = 0; i < n; i++) GAO
            now = false;
            for (int i = n - 1; i >= 0; i--) GAO
        }

        int ans = 0;
        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (!G[i][j] && !W[i][j] && !f[i][j]) ans++;
        return ans;
    }
};


// 作者：tsreaper
// 链接：https://leetcode.cn/problems/count-unguarded-cells-in-the-grid/solution/by-tsreaper-znyl/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。