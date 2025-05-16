class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int K, vector<vector<int>>& queries) {
        int n = nums.size();
        for (int &x : nums) x %= K;

        // 线段树里一个区间要维护的值
        struct Node {
            long long prod, cnt[5];

            void init(int x) {
                memset(cnt, 0, sizeof(cnt));
                prod = x;
                cnt[x] = 1;
            }
        };
        Node tree[n * 4 + 5];

        // 合并两个子区间
        auto merge = [&](Node nl, Node nr) {
            Node ret;
            ret.prod = nl.prod * nr.prod % K;
            for (int k = 0; k < K; k++) ret.cnt[k] = nl.cnt[k];
            for (int k = 0; k < K; k++) ret.cnt[nl.prod * k % K] += nr.cnt[k];
            return ret;
        };

        // 建树
        auto build = [&](this auto &&build, int id, int l, int r) -> void {
            if (l == r) {
                tree[id].init(nums[l]);
            } else {
                int nxt = id << 1, mid = (l + r) >> 1;
                build(nxt, l, mid); build(nxt | 1, mid + 1, r);
                tree[id] = merge(tree[nxt], tree[nxt | 1]);
            }
        };

        // 单点修改
        auto modify = [&](this auto &&modify, int id, int l, int r, int qpos, int qv) -> void {
            if (l == r) {
                tree[id].init(qv);
            } else {
                int nxt = id << 1, mid = (l + r) >> 1;
                if (qpos <= mid) modify(nxt, l, mid, qpos, qv);
                else modify(nxt | 1, mid + 1, r, qpos, qv);
                tree[id] = merge(tree[nxt], tree[nxt | 1]);
            }
        };

        // 区间查询
        auto query = [&](this auto &&query, int id, int l, int r, int ql, int qr) -> Node {
            if (ql <= l && r <= qr) return tree[id];
            int nxt = id << 1, mid = (l + r) >> 1;
            if (qr <= mid) return query(nxt, l, mid, ql, qr);
            if (ql > mid) return query(nxt | 1, mid + 1, r, ql, qr);
            return merge(query(nxt, l, mid, ql, qr), query(nxt | 1, mid + 1, r, ql, qr));
        };

        build(1, 0, n - 1);
        vector<int> ans;
        for (auto &qry : queries) {
            modify(1, 0, n - 1, qry[0], qry[1] % K);
            ans.push_back(query(1, 0, n - 1, qry[2], n - 1).cnt[qry[3]]);
        }
        return ans;
    }
};