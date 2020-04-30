import math
class Solution:
    def rob_(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums+[0])
        dp = nums[:2]
        for i,num in enumerate(nums[2:], 2):
            dp[-1], dp[-2] = dp[-2]+num, max(dp[-1],dp[-2])
        return max(dp[-1], dp[-2])
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums+[0])
        return max(self.rob_(nums[1:]),self.rob_(nums[:-1]))