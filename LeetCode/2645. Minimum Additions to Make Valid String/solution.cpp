class Solution {
public:
    int minimumTotalPrice(int n, vector<vector<int>>& edges, vector<int>& price, vector<vector<int>>& trips) {
        // 建图
        vector<int> e[n];
        for (auto &edge : edges) {
            e[edge[0]].push_back(edge[1]);
            e[edge[1]].push_back(edge[0]);
        }

        // qry[i] 表示与节点 i 有关的最近公共祖先询问有哪些
        vector<int> qry[n];
        for (auto &trip : trips) {
            qry[trip[0]].push_back(trip[1]);
            // 有可能 trip[0] == trip[1]，我们要防止重复处理询问
            if (trip[0] != trip[1]) qry[trip[1]].push_back(trip[0]);
        }

        // 并查集
        int root[n];
        for (int i = 0; i < n; i++) root[i] = i;

        // 求并查集的根
        function<int(int)> findroot = [&](int x) {
            if (root[x] != x) root[x] = findroot(root[x]);
            return root[x];
        };

        // 把 x 合并到 y 的集合里
        auto merge = [&](int x, int y) {
            x = findroot(x); y = findroot(y);
            if (x != y) root[x] = y;
        };

        // pa[i]：节点 i 的父节点
        int pa[n];
        // vis[i]：节点 i 在 tarjan 算法中是否被访问过了
        bool vis[n];
        memset(vis, 0, sizeof(vis));
        // delta[i]：如题解所述，是节点 i 对祖先节点的影响
        int delta[n];
        memset(delta, 0, sizeof(delta));

        // tarjan 离线求 lca
        function<void(int, int)> tarjan = [&](int sn, int fa) {
            pa[sn] = fa;
            for (int fn : e[sn]) if (fn != fa) {
                tarjan(fn, sn);
                merge(fn, sn);
            }
            for (int fn : qry[sn]) {
                if (fn == sn) {
                    // 特殊情况：求两个相同点的 lca
                    delta[sn]++;
                    if (fa >= 0) delta[fa]--;
                } if (vis[fn]) {
                    // 如题解所述，更新 delta 的值
                    int a = findroot(fn);
                    delta[sn]++;
                    delta[fn]++;
                    delta[a]--;
                    if (pa[a] >= 0) delta[pa[a]]--;
                }
            }
            vis[sn] = true;
        };
        tarjan(0, -1);

        // 打家劫舍 III
        long long ans = 0;
        long long f[n][2];
        memset(f, 0, sizeof(f));
        // 返回值表示 sn 的子树中所有 delta 值之和
        function<int(int, int)> dp = [&](int sn, int fa) {
            // sm 即为 sn 子树中所有 delta 值之和
            int sm = delta[sn];
            for (int fn : e[sn]) if (fn != fa) {
                sm += dp(fn, sn);
                f[sn][0] += max(f[fn][0], f[fn][1]);
                f[sn][1] += f[fn][0];
            }
            f[sn][1] += 1LL * sm * price[sn] / 2;
            // 顺便算一下总费用
            ans += 1LL * sm * price[sn];
            return sm;
        };
        dp(0, -1);
        // 答案就是总费用减去最大节省费用
        ans -= max(f[0][0], f[0][1]);
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/YQDX7V/view/5QF80Y/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。