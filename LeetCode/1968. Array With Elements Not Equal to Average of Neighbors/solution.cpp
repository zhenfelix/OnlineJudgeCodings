class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector<int> ans(n);
        int ptr = 0;
        for (int i = 0; i < n; i += 2)
            ans[i] = nums[ptr++];
        for (int i = 1; i < n; i += 2)
            ans[i] = nums[ptr++];
        return ans;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/xzKfhg/view/r9MO35/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。