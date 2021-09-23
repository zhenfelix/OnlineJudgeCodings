class Solution {
public:
    int minOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size(), left = 0, right = 0, distinct = 0, res = 0;
        for (; left < n && right < n; left++){
            while (right < n && nums[right] <= nums[left]+n-1){
                if (right == 0 || nums[right] != nums[right-1])
                    distinct++;
                right++;
            }
            res = max(res, distinct);
            if (left == n-1 || nums[left] != nums[left+1])
                distinct--;
        }
        return n-res;
    }
};