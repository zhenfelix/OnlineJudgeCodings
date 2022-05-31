from functools import lru_cache
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        @lru_cache(None)
        def dfs(i, cnt):
            if cnt < 0:
                return float('inf')
            if i < 0:
                return 0
            return min(dfs(i-1, cnt)+int(floor[i]), dfs(i-carpetLen, cnt-1))
        n = len(floor)
        return dfs(n-1, numCarpets)


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        floor = list(map(int, floor))
        n = len(floor)
        dp = floor[:]
        for i in range(1,n):
            dp[i] += dp[i-1]
        for i in range(numCarpets):
            ndp = [float('inf')]*n
            for j in range(n):
                if j < carpetLen:
                    ndp[j] = 0
                else:
                    ndp[j] = min(ndp[j-1]+floor[j], dp[j-carpetLen])
            dp = ndp
        return dp[-1]


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        floor = list(map(int, floor))
        n = len(floor)
        dp = floor[:]
        for i in range(1,n):
            dp[i] += dp[i-1]
        ndp = [float('inf')]*n
        for i in range(numCarpets):
            for j in range(n):
                if j < carpetLen:
                    ndp[j] = 0
                else:
                    ndp[j] = min(ndp[j-1]+floor[j], dp[j-carpetLen])
            dp, ndp = ndp, dp
        return dp[-1]