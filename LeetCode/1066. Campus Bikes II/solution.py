
from functools import lru_cache
class Solution:
    def assignBikes(self, workers, bikes):
        n, m = len(workers), len(bikes)
        def dist(i,j):
            return abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])
        @lru_cache(None)
        def dfs(idx,state):
            if idx == n:
                return 0
            return min(dist(idx,j)+dfs(idx+1,state|(1<<j)) for j in range(m) if (1<<j) & state == 0)
        return dfs(0,0)
                