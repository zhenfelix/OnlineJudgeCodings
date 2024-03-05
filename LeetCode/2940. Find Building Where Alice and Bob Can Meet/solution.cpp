class Solution {
public:
    vector<int> leftmostBuildingQueries(vector<int>& heights, vector<vector<int>>& queries) {
        int n = heights.size();

        vector<array<int, 3>> vec;
        int q = queries.size();
        vector<int> ans(q, -2);
        for (int i = 0; i < q; i++) {
            int a = min(queries[i][0], queries[i][1]), b = max(queries[i][0], queries[i][1]);
            // 处理两种特殊询问
            if (a == b) ans[i] = a;
            else if (heights[a] < heights[b]) ans[i] = b;
            // 剩下的询问加入二维偏序问题
            // 注意排序方式：首先按 heights 从大到小排序，相同 heights 的询问一定要排在数据点之后
            else vec.push_back({-heights[a] - 1, i, b});
        }
        for (int i = 0; i < n; i++) vec.push_back({-heights[i], -1, i});
        sort(vec.begin(), vec.end());

        // 树状数组模板

        const int INF = 1e9;
        int tree[n + 1];
        for (int i = 1;i <= n; i++) tree[i] = INF;

        auto lowbit = [&](int x) { return x & (-x); };

        auto modify = [&](int pos, int val) {
            for (; pos <= n; pos += lowbit(pos)) tree[pos] = min(tree[pos], val);
        };

        auto query = [&](int pos) {
            int ret = INF;
            for (; pos; pos -= lowbit(pos)) ret = min(ret, tree[pos]);
            return ret;
        };

        // 利用树状数组处理二维偏序问题
        for (auto &arr : vec) {
            int tpe = arr[1], idx = arr[2];
            if (tpe == -1) modify(n - idx, idx);
            else {
                ans[tpe] = query(n - idx);
                if (ans[tpe] == INF) ans[tpe] = -1;
            }
        }
        return ans;
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。