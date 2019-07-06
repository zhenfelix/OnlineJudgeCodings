class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp, ans = 0, 0
        for i, x in enumerate(nums):
            if i == 0 or x > nums[i-1]:
                dp += 1
            else:
                dp = 1
            ans = max(ans, dp)
        return ans