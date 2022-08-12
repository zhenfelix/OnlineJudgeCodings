class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        dp = [0]*(m+1)
        dp[0] = 1
        for ch in s:
            for i in range(m)[::-1]:
                if ch == t[i]:
                    dp[i+1] += dp[i]
        return dp[-1]

from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if i < j:
                return 0
            if j == 0:
                return 1
            return dfs(i-1,j) + (dfs(i-1,j-1) if s[i-1]==t[j-1] else 0)
        return dfs(len(s),len(t))


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if i < j:
                return 0
            if j == -1:
                return 1
            res = dfs(i-1,j)
            res += (s[i]==t[j])*dfs(i-1,j-1)
            return res
        return dfs(len(s)-1, len(t)-1)