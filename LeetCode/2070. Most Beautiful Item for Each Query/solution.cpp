class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        int n = items.size(), q = queries.size();
        vector<int> ans(q);
        vector<int> order(q);
        for (int i = 0; i < q; ++i)
            order[i] = i;
        sort(order.begin(), order.end(), [&](int i, int j){
            return queries[i] < queries[j]; 
        });
        sort(items.begin(), items.end());
        int hi = 0, ptr = -1;
        for (int i : order) {
            while (ptr + 1 < n && items[ptr + 1][0] <= queries[i]) 
                hi = max(hi, items[++ptr][1]);
            ans[i] = hi;
        }
        return ans;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/cj4dO9/view/Mwspom/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。