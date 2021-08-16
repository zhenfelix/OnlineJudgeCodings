class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9+7
        dp = [0,0,0,1]
        for x in nums:
            dp[x] *= 2
            dp[x] += dp[x-1]
            dp[x] %= MOD
        return dp[2]