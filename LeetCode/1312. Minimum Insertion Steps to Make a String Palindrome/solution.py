from functools import lru_cache
class Solution:
    def minInsertions(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dfs(i+1,j-1)
            return min(dfs(i+1,j),dfs(i,j-1))+1
        return dfs(0,len(s)-1)