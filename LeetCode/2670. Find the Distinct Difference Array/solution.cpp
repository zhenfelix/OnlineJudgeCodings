class Solution {
public:
    vector<int> distinctDifferenceArray(vector<int>& nums) {
        int n = nums.size();
        
        // 计算 f[i] 表示 nums[0..i] 中不同元素的数目
        int f[n];
        unordered_set<int> st;
        for (int i = 0; i < n; i++) {
            st.insert(nums[i]);
            f[i] = st.size();
        }
        
        // 计算 g[i] 表示 nums[i..n - 1] 中不同元素的数目
        int g[n + 1];
        g[n] = 0;
        st.clear();
        for (int i = n - 1; i >= 0; i--) {
            st.insert(nums[i]);
            g[i] = st.size();
        }
        
        // 计算答案
        vector<int> ans;
        for (int i = 0; i < n; i++) ans.push_back(f[i] - g[i + 1]);
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/FDkyPg/view/8uWFqW/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。