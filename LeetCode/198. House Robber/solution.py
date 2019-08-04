import math

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n < 3:
            return max(nums)
        dp = [-math.inf]*n
        dp[0], dp[1] = nums[0], nums[1]
        for i,num in enumerate(nums):
            if i+2 < n and dp[i+2] < dp[i]+nums[i+2]:
                dp[i+2] = dp[i]+nums[i+2]
            if i+3 < n and dp[i+3] < dp[i]+nums[i+3]:
                dp[i+3] = dp[i]+nums[i+3]
        return max(dp[-1], dp[-2])