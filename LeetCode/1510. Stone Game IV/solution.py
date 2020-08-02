from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        i = 1
        while i*i <= n:
            if not self.winnerSquareGame(n-i*i):
                return True
            i += 1
        return False


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        for i in range(1,n+1):
            j = 1
            while j*j <= i:
                if not dp[i-j*j]:
                    dp[i] = True
                    break
                j += 1
        return dp[-1]