// 线性递推常见优化：压缩第一维的空间
bitset<600> f[2][300];

class Solution {
public:
    int maxWeight(int n, vector<vector<int>>& edges, int K, int T) {
        // 建图
        vector<int> e[n], v[n];
        for (auto &edge : edges) {
            e[edge[0]].push_back(edge[1]);
            v[edge[0]].push_back(edge[2]);
        }

        for (int i = 0; i < n; i++) f[0][i].reset();
        for (int i = 0; i < n; i++) f[0][i][0] = true;
        for (int k = 0; k < K; k++) {
            for (int sn = 0; sn < n; sn++) f[k & 1 ^ 1][sn].reset();
            for (int sn = 0; sn < n; sn++) for (int i = 0; i < e[sn].size(); i++) {
                int fn = e[sn][i];
                // 普通 DP 方程里对最后一维的加法，相当于 bitset 里的左移
                // 请读者仔细体会为什么是这样对应
                f[k & 1 ^ 1][fn] |= f[k & 1][sn] << v[sn][i];
            }
        }

        // 枚举最大权值
        for (int t = T - 1; t >= 0; t--) for (int sn = 0; sn < n; sn++) if (f[K & 1][sn][t]) return t;
        return -1;
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/maximum-weighted-k-edge-path/solutions/3673713/di-tui-bitset-you-hua-by-tsreaper-t9oa/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。