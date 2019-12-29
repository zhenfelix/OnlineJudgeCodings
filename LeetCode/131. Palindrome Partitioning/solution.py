# from functools import lru_cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # @lru_cache(None)
        def dfs(i,j):
            if i > j:
                return [[]]
            if i == j:
                return [[s[i]]]
            res = []
            for k in range(i,j+1):
                if s[i:k+1] == s[i:k+1][::-1]:
                    nxts = dfs(k+1,j)
                    for nxt in nxts:
                        res.append([s[i:k+1]]+nxt)
            return res
        return dfs(0,len(s)-1)