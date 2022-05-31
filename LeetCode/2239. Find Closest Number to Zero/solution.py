class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = -float('inf')
        for x in nums:
            if abs(x) < abs(ans):
                ans = x
            elif abs(x) == abs(ans) and x > ans:
                ans = x
        return ans 

