from functools import lru_cache
class Solution:
    def keyboard(self, K: int, N: int) -> int:
        MOD = 10**9+7
        @lru_cache(None)
        def dfs(k,n,c):
            if c == 1:
                return 0 if n > k else 1
            if n == 1:
                return c 
            return sum(dp[n][i]*dfs(k,n-i,c-1) for i in range(min(k,n)+1))%MOD
        dp = [[1]*(N+1) for _ in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,i):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        return dfs(K,N,26)