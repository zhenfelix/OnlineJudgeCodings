class Solution:
    def waysToDistribute(self, N: int, K: int) -> int:
        MOD = 10**9+7
        dp = [[1]*(N+1) for _ in range(K+1)]
        for k in range(2,K+1):
            for n in range(k+1,N+1):
                dp[k][n] = dp[k-1][n-1] + k*dp[k][n-1]
                dp[k][n] %= MOD
        return dp[K][N]

