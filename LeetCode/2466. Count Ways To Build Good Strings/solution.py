class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9+7
        f = [0]*(high+1)
        f[0] = 1
        ans = 0
        for i in range(1,high+1):
            if i-zero >= 0: f[i] = (f[i-zero]+f[i])%MOD
            if i-one >= 0: f[i] = (f[i-one]+f[i])%MOD
            if i >= low: ans = (ans+f[i])%MOD
        return ans

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9+7
        @lru_cache(None)
        def dfs(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            return (dfs(n-zero)+dfs(n-one))%MOD 
        ans = 0
        for i in range(low,high+1):
            ans += dfs(i)
            ans %= MOD
        return ans