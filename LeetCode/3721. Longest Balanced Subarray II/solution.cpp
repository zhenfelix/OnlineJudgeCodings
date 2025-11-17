class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size();

        // 线段树节点，记录当前区间前缀和的最小值与最大值
        struct Node {
            int mn, mx, lazy;

            void apply(int x) {
                mn += x;
                mx += x;
                lazy += x;
            }
        } tree[(n + 1) * 4 + 5];

        auto merge = [&](Node nl, Node nr) {
            return Node {
                min(nl.mn, nr.mn),
                max(nl.mx, nr.mx),
                0
            };
        };

        // 线段树建树
        auto build = [&](this auto &&build, int id, int l, int r) -> void {
            if (l == r) tree[id] = Node {0, 0, 0};
            else {
                int nxt = id << 1, mid = (l + r) >> 1;
                build(nxt, l, mid); build(nxt | 1, mid + 1, r);
                tree[id] = merge(tree[nxt], tree[nxt | 1]);
            }
        };

        // 懒标记下推
        auto down = [&](int id) {
            if (tree[id].lazy == 0) return;
            int nxt = id << 1;
            tree[nxt].apply(tree[id].lazy);
            tree[nxt | 1].apply(tree[id].lazy);
            tree[id].lazy = 0;
        };

        // 给区间 [ql, qr] 的前缀和都加上 qv
        auto modify = [&](this auto &&modify, int id, int l, int r, int ql, int qr, int qv) -> void {
            if (ql <= l && r <= qr) tree[id].apply(qv);
            else {
                down(id);
                int nxt = id << 1, mid = (l + r) >> 1;
                if (ql <= mid) modify(nxt, l, mid, ql, qr, qv);
                if (qr > mid) modify(nxt | 1, mid + 1, r, ql, qr, qv);
                tree[id] = merge(tree[nxt], tree[nxt | 1]);
            }
        };

        // 线段树上二分，求前缀和等于 qv 的最小下标
        auto query = [&](this auto &&query, int id, int l, int r, int qv) -> int {
            if (l == r) return l;
            down(id);
            int nxt = id << 1, mid = (l + r) >> 1;
            // 只要一个区间满足 mn <= qv <= mx，那么一定存在一个等于 qv 的值
            // 为了让下标最小，只要左子区间满足，就去左子区间里拿答案，否则才去右子区间拿答案
            if (tree[nxt].mn <= qv && qv <= tree[nxt].mx) return query(nxt, l, mid, qv);
            else return query(nxt | 1, mid + 1, r, qv);
        };

        build(1, 0, n);
        // now：目前的前缀和
        int ans = 0, now = 0;
        // mp[x]：元素 x 最近出现在哪个下标
        unordered_map<int, int> mp;
        // 枚举子数组右端点
        for (int i = 1; i <= n; i++) {
            int x = nums[i - 1];
            int det = (x & 1 ? 1 : -1);
            if (mp.count(x)) {
                // 元素 x 之前出现过了，把那个位置改成 0
                modify(1, 0, n, mp[x], n, -det);
                now -= det;
            }
            // 把元素 x 当前出现的位置改成 +-1
            mp[x] = i;
            modify(1, 0, n, i, n, det);
            now += det;
            int pos = query(1, 0, n, now);
            ans = max(ans, i - pos);
        }
        return ans;
    }
};