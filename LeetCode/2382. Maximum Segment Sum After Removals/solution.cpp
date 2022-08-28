class Solution {
public:
    vector<long long> maximumSegmentSum(vector<int>& nums, vector<int>& removeQueries) {
        int n = nums.size();
        // 求前缀和，方便我们直接求出区间的和
        vector<long long> f(n + 1);
        for (int i = 1; i <= n; i++) f[i] = f[i - 1] + nums[i - 1];

        // 记录已删除的下标
        set<int> st;
        // 放入下标 0 和 n + 1，这样就无需处理边界情况
        st.insert(0); st.insert(n + 1);
        // 记录所有子段和
        multiset<long long> ms;
        // 一开始只有一个子段和，也就是整个数组之和
        ms.insert(f[n]);
        vector<long long> ans;
        for (int pos : removeQueries) {
            pos++;
            // 找出第一个比 pos 大的已删除下标 R，以及最后一个比 pos 小的已删除下标 L
            auto it = st.upper_bound(pos);
            int L = *prev(it), R = *it;
            // 删除下标 pos，把它也放入 st 中
            st.insert(pos);
            // 删除子段 [L + 1, R - 1] 的和
            ms.erase(ms.find(f[R - 1] - f[L]));
            // 加入新子段 [L + 1, pos - 1] 的和
            if (pos - L - 1 > 0) ms.insert(f[pos - 1] - f[L]);
            // 加入新子段 [pos + 1, R - 1] 的和
            if (R - pos - 1 > 0) ms.insert(f[R - 1] - f[pos]);
            // 求出最大的子段和
            if (ms.empty()) ans.push_back(0);
            else ans.push_back(*prev(ms.end()));
        }
        return ans;
    }
};


// 作者：TsReaper
// 链接：https://leetcode.cn/circle/discuss/oZvJdG/view/sKjmHf/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。