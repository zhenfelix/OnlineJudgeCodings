
class Solution {
public:
    int minDifference(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int left = 3, right = n-1, res = INT_MAX;
        if (left >= right)
            return 0;
        for (; left >= 0; left--, right--)
            res = min(res, nums[right]-nums[left]);
        return res;
    }
};