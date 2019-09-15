class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dp0, dp1, res = 0, 0, 0
        for num in nums:
            if num == 0:
                dp0, dp1 = 0, dp0+1
            else:
                dp0, dp1 = dp0+1, dp1+1
            res = max(res, dp0, dp1)
        return res