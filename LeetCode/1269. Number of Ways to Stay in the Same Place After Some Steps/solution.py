# from functools import lru_cache
# class Solution:
#     def numWays(self, steps: int, arrLen: int) -> int:
#         @lru_cache(None)
#         def dfs(step, idx):
#             if idx < 0 or idx >= arrLen:
#                 return 0
#             if step == 0:
#                 return 1 if idx == 0 else 0            
#             return dfs(step-1, idx) + dfs(step-1, idx+1) + dfs(step-1, idx-1)
#         return dfs(steps, 0)%(10**9+7)

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [0]*min(arrLen,steps)
        n = len(dp)
        dp[0] = 1
        for _ in range(steps):
            dp = [dp[i]+(dp[i-1] if i-1 >= 0 else 0)+(dp[i+1] if i+1 < n else 0) for i in range(n)]
        return dp[0]%(10**9+7)