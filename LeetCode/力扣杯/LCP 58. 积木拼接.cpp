class Solution {
    int n;
    vector<vector<string>> shapes;
    // 整个立方体有哪些位置被占用了
    bool A[10][10][10];
    // 哪些面被占用了
    short used[6];

    // 每个面的起始位置
    int CUBE_BASE[6][3] = {
        0, 0, 0,
        0, 0, 1,
        1, 0, 1,
        0, 0, 1,
        0, 0, 1,
        0, 1, 1
    };
    // 每个面 xyz 的增加“方向”
    int CUBE_DIR[6][6] = {
        1, 0, 0, 0, 1, 0,
        1, 0, 0, 0, 1, 0,
        0, 0, -1, 0, 1, 0,
        0, 0, -1, 0, 1, 0,
        0, 0, -1, 1, 0, 0,
        0, 0, -1, 1, 0, 0
    };

    // 形状旋转后的起始位置
    int SHAPE_BASE[4][2] = {0, 0, 0, 1, 1, 0, 1, 1};
    // 形状旋转后行和列的增加“方向”
    int SHAPE_DIR[4][2] = {1, 1, 1, -1, -1, 1, -1, -1};

    // x：哪个形状
    // k：哪个面
    // s：哪种旋转
    // rc：行列是否交换
    // modify：0 = 检查是否占用；1 = 占用；-1 = 取消占用
    bool gao(int x, int k, int s, bool rc, int modify) {
        for (int a = 0; a < n; a++) for (int b = 0; b < n; b++) {
            int i = CUBE_BASE[k][0] * (n - 1) + CUBE_DIR[k][0] * a + CUBE_DIR[k][3] * b;
            int j = CUBE_BASE[k][1] * (n - 1) + CUBE_DIR[k][1] * a + CUBE_DIR[k][4] * b;
            int z = CUBE_BASE[k][2] * (n - 1) + CUBE_DIR[k][2] * a + CUBE_DIR[k][5] * b;
            int si = SHAPE_BASE[s][0] * (n - 1) + SHAPE_DIR[s][0] * (rc ? b : a);
            int sj = SHAPE_BASE[s][1] * (n - 1) + SHAPE_DIR[s][1] * (rc ? a : b);
            if (shapes[x][si][sj] == '1') {
                if (modify == 1) A[i][j][z] = true;
                else if (modify == -1) A[i][j][z] = false;
                else if (A[i][j][z]) return false;
            }
        }
        return true;
    }

    bool dfs(int x) {
        if (x == 6) return true;
        for (int k = 0; k < 6; k++) if (!used[k]) {
            for (int i = 0; i < 4; i++) for (int j = 0; j <= 1; j++) {
                if (!gao(x, k, i, j, 0)) continue;
                gao(x, k, i, j, 1);
                used[k] = true;
                if (dfs(x + 1)) return true;
                used[k] = false;
                gao(x, k, i, j, -1);
            }
        }
        return false;
    }

public:
    bool composeCube(vector<vector<string>>& shapes) {
        n = shapes[0].size();
        int expected = n * n * n - (n - 2) * (n - 2) * (n - 2);
        int actual = 0;
        for (auto &shape : shapes) for (auto &line : shape) for (char c : line) actual += c - '0';
        if (expected != actual) return false;
        this->shapes = shapes;
        return dfs(0);
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/qoClJa/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。