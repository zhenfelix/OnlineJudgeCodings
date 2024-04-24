class Solution {
public:
    int maxIncreasingCells(vector<vector<int>>& mat) {
        int n = mat.size(), m = mat[0].size();
        const int INF = 1e9;
        int R[n], C[m];
        for (int i = 0; i < n; i++) R[i] = -INF;
        for (int j = 0; j < m; j++) C[j] = -INF;

        typedef pair<int, int> pii;
        // mp[x] 表示值为 x 的所有位置
        map<int, vector<pii>> mp;
        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) mp[mat[i][j]].push_back(pii(i, j));

        int ans = 0;
        // 按值从小到大枚举每个位置
        for (auto &entry : mp) {
            // 这里用来临时存放当前值对 R 和 C 数组的更新
            // 必须把当前值所有位置都处理完以后，才能更新到 R 和 C 数组里
            vector<pii> vecR, vecC;
            // 计算当前值每个位置的答案
            for (pii p : entry.second) {
                int t = max({1, R[p.first] + 1, C[p.second] + 1});
                ans = max(ans, t);
                vecR.push_back(pii(p.first, t));
                vecC.push_back(pii(p.second, t));
            }
            // 把临时存放的影响更新到 R 和 C 数组里
            for (pii p : vecR) R[p.first] = max(R[p.first], p.second);
            for (pii p : vecC) C[p.first] = max(C[p.first], p.second);
        }
        return ans;
    }
};


// 作者：TsReaper
// 链接：https://leetcode.cn/circle/discuss/5eR2p8/view/Acz0TI/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。