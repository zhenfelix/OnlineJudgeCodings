class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        ans = -1
        for x in nums:
            if -x in seen:
                ans = max(ans, abs(x))
            seen.add(x)
        return ans 
