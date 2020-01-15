from functools import lru_cache
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n, m = len(ring), len(key)
        @lru_cache(None)
        def dfs(i,j):
            if j == m:
                return 0
            res = min(dfs(k,j+1)+1+min(abs(k-i),n-abs(k-i)) for k in range(n) if ring[k] == key[j])
            # print(i,j,res)
            return res
        return dfs(0,0)
        