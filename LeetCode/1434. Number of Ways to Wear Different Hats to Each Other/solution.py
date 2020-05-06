from functools import lru_cache
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        M = 10**9+7
        n = len(hats)
        graph = defaultdict(list)
        for p, hs in enumerate(hats):
            for h in hs:
                graph[h].append(p)

        @lru_cache(None)
        def dfs(i,state):
            if state == (1<<n)-1:
                return 1
            if i <= 0:
                return 0
            cnt = dfs(i-1,state)
            for p in graph[i]:
                if (1<<p) & state:
                    continue
                cnt += dfs(i-1,state|(1<<p))
            return cnt%M
        
        return dfs(40,0)