from functools import lru_cache
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n, MOD = len(locations), 10**9+7
        @lru_cache(None)
        def dfs(cur, cap):
            if cap < 0:
                return 0
            res = 0
            if cur == finish:
                res += 1
            for nxt in range(n):
                if nxt == cur:
                    continue
                res += dfs(nxt, cap-abs(locations[cur]-locations[nxt]))
                res %= MOD
            return res 
        return dfs(start, fuel)