from functools import lru_cache
class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        @lru_cache(None)
        def dfs(pre, i):
            if i == n:
                return True
            for j in range(i+1, n+1):
                if int(s[i:j]) == pre-1 and dfs(pre-1, j):
                    return True
            return False
        return any(dfs(int(s[:i]), i) for i in range(1,n))