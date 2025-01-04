class Solution {
public:
    long long findMaximumScore(vector<int>& nums) {
        long long ans = 0;
        int mx = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            ans += mx;
            mx = max(mx, nums[i]);
        }
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/vwU4t4/view/KvmYvE/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。