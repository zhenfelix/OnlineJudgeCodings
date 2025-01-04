class Solution {
public:
    vector<int> countOfPeaks(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();

        // 树状数组模板开始

        int tree[n];
        memset(tree, 0, sizeof(tree));

        auto lb = [&](int x) { return x & (-x); };

        auto add = [&](int pos, int val) {
            for (; pos < n; pos += lb(pos)) tree[pos] += val;
        };

        auto query = [&](int pos) {
            if (pos <= 0) return 0;
            int ret = 0;
            for (; pos; pos -= lb(pos)) ret += tree[pos];
            return ret;
        };

        // 树状数组模板结束
        
        int flag[n];
        memset(flag, 0, sizeof(flag));

        // 重新计算下标 i 是否为峰值
        auto recalc = [&](int i) {
            if (i <= 0 || i >= n - 1) return;
            add(i, -flag[i]);
            flag[i] = (nums[i] > nums[i - 1] && nums[i] > nums[i + 1] ? 1 : 0);
            add(i, flag[i]);
        };

        // 初始化每个位置的峰值情况
        for (int i = 1; i + 1 < n; i++) recalc(i);

        vector<int> ans;
        for (auto &qry : queries) {
            if (qry[0] == 1) {
                // 根据题目要求，子数组的首尾元素均不是峰值，因此询问区间的头尾需要各缩小 1
                int L = qry[1] + 1, R = qry[2] - 1;
                if (L > R) ans.push_back(0);
                else ans.push_back(query(R) - query(L - 1));
            } else {
                int idx = qry[1], val = qry[2];
                nums[idx] = val;
                // 直接重算三个元素的峰值情况
                for (int d = -1; d <= 1; d++) recalc(idx + d);
            }
        }
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/ZOlvS4/view/MSmBUv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。