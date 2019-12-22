from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            res = dfs(i+1)
            if i < n-1 and int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            return res

        return dfs(0)