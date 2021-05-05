bool f[110][51][51][2][3];

class Solution {
private:
    static constexpr int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
public:
    bool escapeMaze(vector<vector<string>>& maze) {
        int m = maze[0].size();
        int n = maze[0][0].size();
        if (m == 1 && n == 1) {
            return true;
        }
        
        int k = maze.size();
        memset(f, false, sizeof(f));
        f[0][0][0][0][0] = true;
        
        for (int r = 0; r < k - 1; ++r) {
            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    for (int u1 = 0; u1 < 2; ++u1) {
                        for (int v1 = 0; v1 < 3; ++v1) {
                            if (!f[r][i][j][u1][v1]) {
                                continue;
                            }
                            // move
                            for (int d = 0; d < 4; ++d) {
                                int ni = i + dirs[d][0];
                                int nj = j + dirs[d][1];
                                if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                                    if (maze[r + 1][ni][nj] == '.') {
                                        f[r + 1][ni][nj][u1][v1 ? 2 : 0] = true;
                                    }
                                    else {
                                        if (!u1)
                                            f[r + 1][ni][nj][1][v1 ? 2 : 0] = true;
                                        if (!v1)
                                            f[r + 1][ni][nj][u1][1] = true;
                                    }
                                }
                            }
                            // stand
                            if (maze[r + 1][i][j] == '.') {
                                f[r + 1][i][j][u1][v1] = true;
                            }
                            else {
                                if (v1 == 1)
                                    f[r + 1][i][j][u1][v1] = true;
                                if (!u1) 
                                    f[r + 1][i][j][1][v1] = true;
                                if (!v1)
                                    f[r + 1][i][j][u1][1] = true;
                                
                            }
                        }
                    }
                }
            }

        }
        
        for (int r = 0; r < k; ++r) {
            for (int u1 = 0; u1 < 2; ++u1) {
                for (int v1 = 0; v1 < 3; ++v1) {
                    if (f[r][m - 1][n - 1][u1][v1]) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};