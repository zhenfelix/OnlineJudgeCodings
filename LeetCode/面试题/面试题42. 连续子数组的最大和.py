class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum, cursum, res = 0, 0, -float('inf')
        for num in nums:
            cursum += num
            res = max(res, cursum-presum)
            presum = min(presum, cursum)
        return res
