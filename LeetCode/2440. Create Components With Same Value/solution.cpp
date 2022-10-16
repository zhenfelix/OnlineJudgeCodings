class Solution {
public:
    int componentValue(vector<int>& A, vector<vector<int>>& edges) {
        int n = A.size();
        
        // 建图
        vector<int> e[n];
        for (auto &edge : edges) {
            e[edge[0]].push_back(edge[1]);
            e[edge[1]].push_back(edge[0]);
        }

        // 计算每个子树的权值之和
        int f[n];
        function<void(int, int)> dfs1 = [&](int sn, int fa) {
            f[sn] = A[sn];
            for (int fn : e[sn]) if (fn != fa) {
                dfs1(fn, sn);
                f[sn] += f[fn];
            }
        };
        dfs1(0, -1);

        // 检查每个连通块的权值是否都是 X
        function<bool(int, int, int)> dfs2 = [&](int sn, int fa, int X) {
            int sm = A[sn];
            for (int fn : e[sn]) if (fn != fa) {
                // 子树里已经检查失败了，直接返回失败
                if (!dfs2(fn, sn, X)) return false;
                // 边 sn -> fn 不能被删除
                // 把 fn 所处连通块的值加到 sn 所处连通块的值（也就是 sm）
                if (f[fn] % X != 0) sm += f[fn] % X;
            }
            // 检查 sn 所处连通块的值是否符合要求
            return sm <= X ? true : false;
        };

        // 枚举连通块的权值
        for (int i = 1; i <= f[0]; i++)
            if (f[0] % i == 0 && dfs2(0, -1, i)) return f[0] / i - 1;
        return 0;
    }
};



作者：tsreaper
链接：https://leetcode.cn/problems/create-components-with-same-value/solution/by-tsreaper-700z/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。