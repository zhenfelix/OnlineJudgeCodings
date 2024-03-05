class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n = nums.size();
        typedef pair<int, int> pii;
        // 把所有元素从小到大排序，要记录一下原来的下标
        vector<pii> vec;
        for (int i = 0; i < n; i++) vec.push_back(pii(nums[i], i));
        sort(vec.begin(), vec.end());

        // 把所有元素切成若干子段，子段内的相邻元素之差不超过 limit
        vector<vector<pii>> segs;
        int last = -limit;
        for (int i = 0; i < n; i++) {
            if (vec[i].first - last > limit) segs.push_back({});
            segs.back().push_back(vec[i]);
            last = vec[i].first;
        }

        vector<int> ans(n);
        // 对每个子段分别从小到大排序，填回序列中
        for (auto &seg : segs) {
            vector<int> pos;
            for (auto &p : seg) pos.push_back(p.second);
            sort(pos.begin(), pos.end());
            for (int i = 0; i < seg.size(); i++) ans[pos[i]] = seg[i].first;
        }
        return ans;
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。