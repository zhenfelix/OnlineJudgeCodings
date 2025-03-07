class Solution {
public:
    int maxDifference(string s, int K) {
        int n = s.size();

        // f[i][c]：前 i 个字符中，字符 c 出现了几次
        int f[n + 1][5];
        for (int j = 0; j < 5; j++) f[0][j] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < 5; j++) f[i][j] = f[i - 1][j];
            f[i][s[i - 1] - '0']++;
        }

        const int INF = 1e9;
        // 求出奇数频率的字符为 x，偶数频率的字符为 y 的情况下的最大子数组和
        auto gao = [&](int x, int y) {
            int ret = -INF;
            // g[0/1][0/1] 表示 x 和 y 在前缀里分别出现奇（偶）数次的最小前缀和
            int g[2][2];
            for (int i = 0; i < 2; i++) for (int j = 0; j < 2; j++) g[i][j] = INF;
            // 枚举子数组的右端点 i
            // j 是一个单调指针，表示子数组的左端点最大可以到哪
            for (int i = 1, j = 0; i <= n; i++) {
                while (i - j >= K && f[i][x] != f[j][x] && f[i][y] != f[j][y]) {
                    int &t = g[f[j][x] & 1][f[j][y] & 1];
                    t = min(t, f[j][x] - f[j][y]);
                    j++;
                }
                int now = f[i][x] - f[i][y];
                // x 要出现奇数次，所以在前缀里频率的奇偶性必须不同
                // y 要出现偶数次，所以在前缀里频率的奇偶性必须相同
                ret = max(ret, now - g[f[i][x] & 1 ^ 1][f[i][y] & 1]);
            }
            return ret;
        };

        int ans = -INF;
        // 枚举两种字符分别是哪个
        for (int i = 0; i < 5; i++) for (int j = 0; j < 5; j++) ans = max(ans, gao(i, j));
        return ans;
    }
};

// 作者：TsReaper
// 链接：https://leetcode.cn/problems/maximum-difference-between-even-and-odd-frequency-ii/solutions/3061769/mei-ju-qian-zhui-he-by-tsreaper-vzml/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。