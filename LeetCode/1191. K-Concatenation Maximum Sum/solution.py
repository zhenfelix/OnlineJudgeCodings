class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        preSum, minSum, maxSum, res = 0, 0, -float('inf'), 0
        M = 10**9 + 7
        for a in arr:
            preSum += a
            res = max(preSum-minSum, res)
            minSum = min(minSum, preSum)
            maxSum = max(maxSum, preSum)
        
        if k == 1:
            return res%M
        if preSum < 0:
            return max(maxSum-minSum+preSum, res)%M
        else:
            return (maxSum-minSum+(k-1)*preSum)%M
        