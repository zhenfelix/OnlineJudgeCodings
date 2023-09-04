class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        dp = [0]*2 
        cur = 0
        for i in range(n)[::-1]:
            j = nums[i]%2 
            cur = max(dp[j],dp[1-j]-x)+nums[i]
            dp[j] = max(dp[j],cur)
        return cur 