# class Solution:
#     def minDays(self, n: int) -> int:
#         dp = {}
#         def dfs(n: int) -> int:
#             if n <= 1:
#                 return n;
#             if (n not in dp):
#                 dp[n] = 1 + min(n % 2 + dfs(n // 2), n % 3 + dfs(n // 3));
#             return dp[n];
#         return dfs(n)

class Solution:
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n == 0:
            return 0
        res = n 
        res = min(res, 1+self.minDays(n//2)+n%2)
        res = min(res, 1+self.minDays(n//3)+n%3)
        # print(n,res)
        return res

from functools import lru_cache
class Solution:
    def minDays(self, n: int) -> int:
        
        @lru_cache(None)
        def helper(n, one=0):
            if one >= 3:
                return math.inf
            if n < 1: return n
            
            prev = helper(n - 1, one + 1)
            if not n % 2:
                prev = min(prev, helper(n // 2))
            if not n % 3:                
                prev = min(prev, helper(n // 3))
            return prev + 1                
        
        return helper(n)