# from functools import lru_cache
# class Solution:
#     def integerBreak(self, n: int) -> int:
#         @lru_cache(None)
#         def dfs(x):
#             if x == 1:
#                 return 1
#             return max(max(dfs(i),i)*max(dfs(x-i),x-i) for i in range(1,x//2+1))
#         return dfs(n)

# class Solution:
#     def integerBreak(self, n: int) -> int:
#         dp = [0]*(n+1)
#         dp[1] = 1
#         for x in range(2,n+1):
#             dp[x] = max(max(dp[i],i)*max(dp[x-i],x-i) for i in range(1,x//2+1))
#         return dp[-1]


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        res *= n
        return res

import functools
class Solution:
    @functools.lru_cache(None)
    def cuttingRope(self, n: int) -> int:
        if n <= 2:
            return 1
        return max(max(i,self.cuttingRope(i))*max(n-i,self.cuttingRope(n-i)) for i in range(1,n//2+1))
