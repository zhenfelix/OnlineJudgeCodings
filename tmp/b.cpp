class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = edges.size() + 1;
        // 建图
        vector<int> e[n], v[n];
        for (auto &edge : edges) {
            e[edge[0]].push_back(edge[1]); v[edge[0]].push_back(edge[2]);
            e[edge[1]].push_back(edge[0]); v[edge[1]].push_back(edge[2]);
        }

        array<int, 2> ans = {-1, 0};
        // mp[c] 是一个 vector，保存了 DFS 过程中哪些深度出现了颜色 c，vector 的末尾是最大的深度
        unordered_map<int, vector<int>> mp;
        // vec[d] 保存了从根到深度为 d 的节点的路径长度
        int vec[n];
        // sm：根到当前节点（sn）的路径长度
        // lim：起点的深度最小可以到多少
        auto dfs = [&](this auto &&dfs, int sn, int fa, int sm, int d, int lim1, int lim2) -> void {
            // 把根到当前节点的路径长度压入栈，方便后续的 DFS 过程使用
            vec[d] = sm;
            // DFS 栈中出现了和 sn 相同颜色的节点 u，起点下移到 u 的下一个节点，即起点的深度移动到 u 的深度 + 1
            if (mp[nums[sn]].size() > 0) {
                int t = mp[nums[sn]].back() + 1;
                if (t > lim1) lim2 = lim1, lim1 = t;
                else if (t > lim2) lim2 = t;
            }
            // 计算从深度 lim 到当前深度的路径长度和节点数量
            // 出于未知原因，在力扣使用 max 对比两个 array 或者 pair 非常慢，因此需要拆开来比较
            int x = sm - vec[lim2], y = d - lim2 + 1;
            if (x > ans[0]) ans[0] = x, ans[1] = y;
            else if (x == ans[0] && y < ans[1]) ans[1] = y;

            // 把当前节点的颜色压入栈，方便后续的 DFS 过程使用
            mp[nums[sn]].push_back(d);

            // DFS 进入子节点
            for (int i = 0; i < e[sn].size(); i++) {
                int fn = e[sn][i];
                if (fn == fa) continue;
                dfs(fn, sn, sm + v[sn][i], d + 1, lim1, lim2);
            }

            // 当前节点退栈
            mp[nums[sn]].pop_back();
        };
        dfs(0, -1, 0, 0, 0, 0);
        return {ans[0], ans[1]};
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/longest-special-path-ii/solutions/3613634/dfs-by-tsreaper-8e8z/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。