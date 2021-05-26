class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9+7
        dp = [[0]*(k+1) for _ in range(n+1)]
        for i in range(k+1):
            dp[i][i] = 1
        for i in range(2,n+1):
            dp[i][1] = (i-1)*dp[i-1][1]
            dp[i][1] %= MOD
        for j in range(2,k+1):
            for i in range(j+1,n+1):
                dp[i][j] = dp[i-1][j-1] + (i-1)*dp[i-1][j]
                dp[i][j] %= MOD
        return dp[-1][-1]