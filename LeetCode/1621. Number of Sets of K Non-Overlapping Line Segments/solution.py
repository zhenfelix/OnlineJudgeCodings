from functools import lru_cache
class Solution:
    def numberOfSets(self, N: int, K: int) -> int:
        MOD = 10**9 + 7
        @lru_cache(None)
        def dfs(n,k,empty):
            if k == 0:
                return (n >= 1 and empty)
            if n == 1:
                return 0
            if empty:
                res = dfs(n-1,k,empty) + dfs(n-1,k,not empty)
            else:
                res = dfs(n-1,k,empty) + dfs(n-1,k-1,empty) + dfs(n-1,k-1,not empty)
            return res%MOD
        return dfs(N+1,K,True)


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, k * 2) % (10**9 + 7)
