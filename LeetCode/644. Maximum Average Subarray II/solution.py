class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        lo, hi = min(nums), max(nums)
        presums = [0]
        for x in nums:
            presums.append(presums[-1]+x)
        while hi-lo >= 10**-5:
            mid = (lo+hi)/2
            mi = float('inf')
            flag = False
            for i in range(k,n+1):
                mi = min(mi, presums[i-k]-mid*(i-k))
                if presums[i]-mid*i >= mi:
                    flag = True
                    break
            if flag:
                lo = mid
            else:
                hi = mid
        return (lo+hi)/2




# http://buttercola.blogspot.com/2019/03/lintcode-617-maximum-average-subarray-ii.html

import math

class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        def isPossible(target):
            rightSum, leftSum, minleftSum = 0, 0, math.inf
            for i, num in enumerate(nums):
                rightSum += num - target
                if i >= k-1:
                    if i >= k:
                        leftSum += nums[i-k] - target
                    minleftSum = min(minleftSum, leftSum)
                    if rightSum - minleftSum > 0:
                        return True
            return False


        lo, hi = min(nums), max(nums)
        while lo + 1e-5 < hi:
            mid = (lo + hi)/2
            if isPossible(mid):
                lo = mid
            else:
                hi = mid

        return hi


