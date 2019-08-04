import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, psum, pmin = -math.inf, 0, 0
        for x in nums:
            psum += x
            ans = max(ans, psum-pmin)
            pmin = min(pmin, psum)
        return ans