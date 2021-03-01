import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, psum, pmin = -math.inf, 0, 0
        for x in nums:
            psum += x
            ans = max(ans, psum-pmin)
            pmin = min(pmin, psum)
        return ans


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum, cursum, res = 0, 0, -float('inf')
        for num in nums:
            cursum += num
            res = max(res, cursum-presum)
            presum = min(presum, cursum)
        return res


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, res = nums[0], nums[0]
        for i in range(1,len(nums)):
            cur = max(cur, 0)
            cur += nums[i]
            res = max(res, cur)
        return res 