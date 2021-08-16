class Solution {
public:
    // 正序，从左至右，八连通
    int dirs[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    // 最左侧出发可连通水域
    // set<pair<int, int>> visited;
    // // 最左侧出发暂未连通水域
    // set<pair<int, int>> wait;
    // // 增加连通水域，根据九宫格dfs
    bool dfs(int x, int y, int row, int col, vector<vector<bool>> &visited, vector<vector<bool>> &wait){
        if (y == col-1) return true;
        for(int i = 0; i < 8; i++){
            int new_x = x + dirs[i][0], new_y = y + dirs[i][1];
            if (new_x < 0 || new_x >= row || new_y < 0 || new_y >= col)
                        continue;
            if (wait[new_x][new_y]){
                wait[new_x][new_y] = false;
                visited[new_x][new_y] = true;
                if (dfs(new_x, new_y, row, col, visited, wait)) return true;
            }
        }
        return false;
    }
    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        // 依此遍历cells
        vector<vector<bool>> visited(row, vector<bool>(col, false));
        vector<vector<bool>> wait(row, vector<bool>(col, false));
        for(int d = 0; d < row * col; d++){
            int x = cells[d][0], y = cells[d][1];
            x--;y--;
            bool flag = false;
            // 最左侧出发
            if (y == 0) flag = true;
            // 非最左侧，根据九宫格判断能否连通
            else{
                for(int i = 0; i < 8; i++){
                    int new_x = x + dirs[i][0], new_y = y + dirs[i][1];
                    if (new_x < 0 || new_x >= row || new_y < 0 || new_y >= col)
                        continue;
                    if (visited[new_x][new_y]){
                        flag = true;
                        break;
                    }
                }
            }
            // 若当前水域可连通，则通过dfs尝试取出wait内的水域
            if (flag){
                visited[x][y] = true;
                if (dfs(x, y, row, col, visited, wait)) return d;
            }
            // 暂未连通，丢入wait
            else{
                wait[x][y] = true;
            }
        }
        // 不可能
        return -1;
    }
};


// 作者：half-empty
// 链接：https://leetcode-cn.com/problems/last-day-where-you-can-still-cross/solution/onzheng-xu-bian-li-si-lu-by-half-empty-9ko3/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



const int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

class Solution {
public:
    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        int lo = 0, hi = row * col;
        while (lo <= hi) {
            int mid = (lo + hi) >> 1;
            vector<vector<bool>> mat(row, vector<bool>(col, true)), vis(row, vector<bool>(col));
            for (int i = 0; i < mid; ++i)
                mat[cells[i][0] - 1][cells[i][1] - 1] = false;
            queue<pair<int, int>> q;
            for (int i = 0; i < col; ++i)
                if (mat[0][i])
                    q.emplace(0, i), vis[0][i] = true;
            bool can = false;
            while (!q.empty()) {
                auto [r, c] = q.front();
                q.pop();
                if (r == row - 1) {
                    can = true;
                    break;
                }
                for (int k = 0; k < 4; ++k) {
                    int nr = r + d[k][0], nc = c + d[k][1];
                    if (nr >= 0 && nr < row && nc >= 0 && nc < col && mat[nr][nc] && !vis[nr][nc]) {
                        vis[nr][nc] = true;
                        q.emplace(nr, nc);
                    }
                }
            }
            if (can)
                lo = mid + 1;
            else
                hi = mid - 1;
        }
        return hi;
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/xzKfhg/view/r9MO35/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


const int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

class UnionFind {
  int n;
  vector<int> parent, size;

public:
  UnionFind(int n) {
    this->n = n;
    parent = vector<int>(n);
    size = vector<int>(n, 1);
    for (int i = 0; i < n; ++i)
      parent[i] = i;
  }

  int find(int idx) {
    if (parent[idx] == idx)
      return idx;
    return parent[idx] = find(parent[idx]);
  }

  void connect(int a, int b) {
    int fa = find(a), fb = find(b);
    if (fa != fb) {
      if (size[fa] > size[fb]) {
        parent[fb] = fa;
        size[fa] += size[fb];
      } else {
        parent[fa] = fb;
        size[fb] += size[fa];
      }
    }
  }
};

class Solution {
public:
    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        UnionFind uf(row * col + 2);
        int S = row * col, T = row * col + 1;
        vector<vector<bool>> exist(row, vector<bool>(col));
        for (int i = row * col - 1; i >= 0; --i) {
            int r = cells[i][0] - 1, c = cells[i][1] - 1;
            if (r == 0)
                uf.connect(S, c);
            if (r == row - 1)
                uf.connect(T, r * col + c);
            exist[r][c] = true;
            for (int k = 0; k < 4; ++k) {
                int nr = r + d[k][0], nc = c + d[k][1];
                if (nr >= 0 && nr < row && nc >= 0 && nc < col && exist[nr][nc])
                    uf.connect(r * col + c, nr * col + nc);
            }
            if (uf.find(S) == uf.find(T))
                return i;
        }
        
        return -1; // Should not return from here.
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/xzKfhg/view/r9MO35/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。