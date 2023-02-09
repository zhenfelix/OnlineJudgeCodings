class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9+7 
        n, m = len(grid), len(grid[0])
        dp = [[0]*(m+1) for _ in range(k)]
        dp[0][0] = 1
        for i in range(n):
            ndp = [[0]*(m+1) for _ in range(k)]
            for j in range(m):
                v = grid[i][j]
                for r in range(k):
                    rr = ((r-v)%k+k)%k
                    ndp[r][j] = (ndp[rr][j-1]+dp[rr][j])%MOD 
            dp = ndp

        return dp[0][m-1]


#TLE otherwise
import gc
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        # gc.disable()
        MOD = 10**9+7 
        n, m = len(grid), len(grid[0])
        @lru_cache(None)
        def dfs(i,j,r):
            if i < 0 or j < 0:
                return 0  
            v = grid[i][j]
            r -= v 
            r %= k
            r = (r+k)%k
            if i == 0 and j == 0:
                return 1 if r == 0 else 0
            return (dfs(i-1,j,r)+dfs(i,j-1,r))%MOD
        res = dfs(n-1,m-1,0)
        dfs.cache_clear()
        return res

import gc
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        gc.disable()
        MOD = 10**9+7 
        n, m = len(grid), len(grid[0])
        @lru_cache(None)
        def dfs(i,j,r):
            if i < 0 or j < 0:
                return 0  
            v = grid[i][j]
            r -= v 
            r %= k
            r = (r+k)%k
            if i == 0 and j == 0:
                return 1 if r == 0 else 0
            return (dfs(i-1,j,r)+dfs(i,j-1,r))%MOD
        res = dfs(n-1,m-1,0)
        gc.collect()
        return res