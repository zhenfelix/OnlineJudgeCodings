class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums+[0])
        dp = nums[:2]
        for i,num in enumerate(nums[2:], 2):
            dp[-1], dp[-2] = dp[-2]+num, max(dp[-1],dp[-2])
        return max(dp[-1], dp[-2])