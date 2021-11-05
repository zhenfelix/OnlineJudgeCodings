from functools import lru_cache

class Solution:
    def securityCheck(self, capacities: List[int], k: int) -> int:
        n = len(capacities)
        MOD = 1000000007
        capacities = [cap-1 for cap in capacities]
        suffix = [cap for cap in capacities]
        for i in range(n-1)[::-1]:
            suffix[i] += suffix[i+1]
        

        @lru_cache(None)
        def dfs(i, sums):
            if i == n:
                return sums == 0
            if sums < 0 or sums > suffix[i]:
                return 0
            
            return (dfs(i+1,sums-capacities[i])+dfs(i+1,sums))%MOD

        res = dfs(0,k)%MOD
        dfs.cache_clear()

        return res
