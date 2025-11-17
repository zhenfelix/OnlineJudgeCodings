#define MAXN 20
#define MAXL 10
#define MAXE 50
// 这么大的数组开在函数里会爆栈，所以开在全局
int dis[MAXN][MAXN][MAXE + 1][1 << MAXL];

class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int n = classroom.size(), m = classroom[0].size();
        int L = 0, SI, SJ;
        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
            // 给每个垃圾一个 0 ~ 9 的编号
            if (classroom[i][j] == 'L') classroom[i][j] = L + '0', L++;
            // 找一下起点
            else if (classroom[i][j] == 'S') SI = i, SJ = j;
        }
        
        short dir[4][2] = {0, 1, 1, 0, -1, 0, 0, -1};
        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++)
            for (int k = 0; k <= energy; k++) for (int l = 0; l < (1 << L); l++)
                dis[i][j][k][l] = -1;
        // BFS
        queue<array<int, 4>> q;
        q.push({SI, SJ, energy, 0}); dis[SI][SJ][energy][0] = 0;
        while (!q.empty()) {
            auto arr = q.front(); q.pop();
            int i = arr[0], j = arr[1], w = arr[2], msk = arr[3];
            // 已经捡完所有垃圾，返回答案
            if (msk == (1 << L) - 1) return dis[i][j][w][msk];
            // 枚举下一步走的方向
            if (w > 0) for (int k = 0; k < 4; k++) {
                int ii = i + dir[k][0], jj = j + dir[k][1];
                if (ii < 0 || jj < 0 || ii >= n || jj >= m || classroom[ii][jj] == 'X') continue;
                int ww = w - 1, mmsk = msk;
                // 走到 R，恢复所有能量
                if (classroom[ii][jj] == 'R') ww = energy;
                // 走到垃圾，记录在 mask 里
                else if (classroom[ii][jj] >= '0' && classroom[ii][jj] <= '9') mmsk |= 1 << (classroom[ii][jj] - '0');
                if (dis[ii][jj][ww][mmsk] >= 0) continue;
                q.push({ii, jj, ww, mmsk}); dis[ii][jj][ww][mmsk] = dis[i][j][w][msk] + 1;
            }
        }
        // 捡不完垃圾
        return -1;
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/minimum-moves-to-clean-the-classroom/solutions/3690738/bfs-by-tsreaper-d8x2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。