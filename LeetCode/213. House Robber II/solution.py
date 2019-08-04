import math
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n < 3:
            return max(nums)
        dp0 = [-math.inf]*n
        dp1 = [-math.inf]*n
        
        dp0[0], dp1[1], dp1[2] = nums[0], nums[1], nums[2]
        for i,num in enumerate(nums):
            if dp0[i] > -math.inf:
                if i+2 < n and dp0[i+2] < dp0[i]+nums[i+2]:
                    dp0[i+2] = dp0[i]+nums[i+2]
                if i+3 < n and dp0[i+3] < dp0[i]+nums[i+3]:
                    dp0[i+3] = dp0[i]+nums[i+3]

            if dp1[i] > -math.inf:
                if i+2 < n and dp1[i+2] < dp1[i]+nums[i+2]:
                    dp1[i+2] = dp1[i]+nums[i+2]
                if i+3 < n and dp1[i+3] < dp1[i]+nums[i+3]:
                    dp1[i+3] = dp1[i]+nums[i+3]
        # print(dp0)
        # print(dp1)
        return max(dp0[-2], dp0[-3], dp1[-1], dp1[-2])