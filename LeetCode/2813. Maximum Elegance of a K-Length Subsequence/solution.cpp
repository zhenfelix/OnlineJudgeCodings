class Solution {
public:
    long long findMaximumElegance(vector<vector<int>>& items, int K) {
        int n = items.size();
        sort(items.begin(), items.end());

        unordered_set<int> st;
        // 因为我们把所有项目按利润排序过了，所以这个 vector 里装的利润是从大到小的，vector 尾部利润最小
        vector<int> vec;
        long long sm = 0;
        // 选择利润前 k 大的项目
        for (int i = 1; i <= K; i++) {
            int p = items[n - i][0], c = items[n - i][1];
            sm += p;
            // 每个类别中，利润不是最大的项目才在我们的考虑替换的范围内
            if (st.count(c)) vec.push_back(p);
            st.insert(c);
        }

        // 计算当前的答案
        auto calc = [&]() { return sm + (long long) st.size() * (long long) st.size(); };

        long long ans = calc();
        // 按利润从大到小寻找新的类别
        for (int i = K + 1; i <= n && !vec.empty(); i++) {
            int p = items[n - i][0], c = items[n - i][1];
            if (st.count(c)) continue;
            // 发现了新类别
            st.insert(c);
            // 淘汰已选类别中，利润最低，且不是该类别利润最大的项目
            sm -= vec.back(); vec.pop_back();
            sm += p;
            // 更新答案
            ans = max(ans, calc());
        }
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/chtVBq/view/Bd2wEn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。