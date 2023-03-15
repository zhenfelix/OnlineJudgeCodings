class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ans, cur = 0, 0
        nums.sort(reverse = True)
        for a in nums:
            cur += a  
            if cur > 0: ans += 1
        return ans 