class Solution:
    def numberOfWays(self, N: int, x: int) -> int:
        MOD = 10**9+7
        @lru_cache(None)
        def dfs(n,m):
            if n == 0:
                return 1
            if m == 0:
                return 0
            y = m**x 
            ans = dfs(n,m-1)
            if y <= n:
                ans += dfs(n-y,m-1)
            return ans%MOD
        return dfs(N,N)