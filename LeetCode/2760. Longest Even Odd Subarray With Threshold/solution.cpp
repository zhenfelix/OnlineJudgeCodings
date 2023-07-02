class Solution {
public:
    int longestAlternatingSubarray(vector<int>& nums, int threshold) {
        int n = nums.size();
        int ans = 0, cnt = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > threshold) cnt = 0;
            else {
                if (i == 0 || nums[i] % 2 == nums[i - 1] % 2) cnt = 1;
                else cnt++;
                // 这里检查子数组的开头是奇数还是偶数，如果是奇数，那么得把开头去掉
                ans = max(ans, cnt - nums[i - cnt + 1] % 2);
            }
        }
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/501Jzp/view/snf1Dd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。