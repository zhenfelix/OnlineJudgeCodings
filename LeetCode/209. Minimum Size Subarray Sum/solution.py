import math

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return 0
        curSum, ans = nums[0], math.inf
        left, right = 0, 0
        while left <= right and right < n:
            # print(ans)
            if curSum < s:
                right += 1
                if right < n:
                    curSum += nums[right]
            else:
                ans = min(ans, right-left+1)
                curSum -= nums[left]
                left +=  1
        if ans == math.inf:
            return 0
        return ans