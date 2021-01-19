class Solution {
private:
    // f[cat_x][cat_y][mouse_x][mouse_y][is_cat_round] = 如果当前玩家必胜那么为 1，否则为 -1
    int f[8][8][8][8][2];
    // 统计每个状态的入度，用于拓扑排序
    int degree[8][8][8][8][2];

    static constexpr int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

public:
    bool canMouseWin(vector<string>& grid, int catJump, int mouseJump) {
        int m = grid.size();
        int n = grid[0].size();

        auto findPosition = [&](char c) -> pair<int, int> {
            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (grid[i][j] == c) {
                        return {i, j};
                    }
                }
            }
            return {-1, -1};
        };

        auto getNeighbors = [&](int x, int y, int bound) -> vector<pair<int, int>> {
            vector<pair<int, int>> ret = {{x, y}};
            for (int d = 0; d < 4; ++d) {
                int xx = x, yy = y;
                for (int _ = 1; _ <= bound; ++_) {
                    xx += dirs[d][0];
                    yy += dirs[d][1];
                    if (xx < 0 || xx >= m || yy < 0 || yy >= n || grid[xx][yy] == '#') {
                        break;
                    }
                    ret.emplace_back(xx, yy);
                }
            }
            return ret;
        };

        auto [cx, cy] = findPosition('C');
        auto [mx, my] = findPosition('M');
        auto [fx, fy] = findPosition('F');

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] != '#') {
                    for (int k = 0; k < m; ++k) {
                        for (int l = 0; l < n; ++l) {
                            if (grid[k][l] != '#') {
                                degree[i][j][k][l][0] = getNeighbors(k, l, mouseJump).size();
                                degree[i][j][k][l][1] = getNeighbors(i, j, catJump).size();
                            }
                        }
                    }
                }
            }
        }

        memset(f, 0, sizeof(f));
        queue<tuple<int, int, int, int, int>> q;

        // 猫和老鼠重合
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] != '#' && grid[i][j] != 'F') {
                    f[i][j][i][j][0] = -1;
                    f[i][j][i][j][1] = 1;
                    q.emplace(i, j, i, j, 0);
                    q.emplace(i, j, i, j, 1);
                }
            }
        }

        // 猫 or 老鼠到达食物
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] != '#' && grid[i][j] != 'F') {
                    f[fx][fy][i][j][0] = -1;
                    f[i][j][fx][fy][1] = -1;
                    q.emplace(fx, fy, i, j, 0);
                    q.emplace(i, j, fx, fy, 1);
                }
            }
        }

        while (!q.empty()) {
            auto [catx, caty, mousex, mousey, op] = q.front();
            q.pop();
            if (op == 1) {
                vector<pair<int, int>> neighbors = getNeighbors(mousex, mousey, mouseJump);
                for (auto [x, y]: neighbors) {
                    --degree[catx][caty][x][y][op ^ 1];
                    if (!f[catx][caty][x][y][op ^ 1]) {
                        if (f[catx][caty][mousex][mousey][op] == -1) {
                            f[catx][caty][x][y][op ^ 1] = 1;
                            q.emplace(catx, caty, x, y, op ^ 1);
                        }
                        else if (degree[catx][caty][x][y][op ^ 1] == 0) {
                            f[catx][caty][x][y][op ^ 1] = -1;
                            q.emplace(catx, caty, x, y, op ^ 1);
                        }
                    }
                }
            }
            else {
                vector<pair<int, int>> neighbors = getNeighbors(catx, caty, catJump);
                for (auto [x, y]: neighbors) {
                    --degree[x][y][mousex][mousey][op ^ 1];
                    if (!f[x][y][mousex][mousey][op ^ 1]) { 
                        if (f[catx][caty][mousex][mousey][op] == -1) {
                            f[x][y][mousex][mousey][op ^ 1] = 1;
                            q.emplace(x, y, mousex, mousey, op ^ 1);
                        }
                        else if (degree[x][y][mousex][mousey][op ^ 1] == 0) {
                            f[x][y][mousex][mousey][op ^ 1] = -1;
                            q.emplace(x, y, mousex, mousey, op ^ 1);
                        }
                    }
                }
            }
        }

        return f[cx][cy][mx][my][0] == 1;
    }
};

