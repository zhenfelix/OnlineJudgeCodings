# from functools import lru_cache
# import sys 

# class Solution:
#     def stoneGameIII(self, stoneValue: List[int]) -> str:
#         sys.setrecursionlimit(10**6)
#         @lru_cache(None)
#         def score(cur,Alice):
#             if cur >= n:
#                 return 0
#             if Alice:
#                 ans = -float('inf')
#                 sums = 0
#                 for i in range(cur,min(n,cur+3)):
#                     sums += stoneValue[i]
#                     ans = max(ans,sums+score(i+1,False))
#                 return ans
#             else:
#                 ans = float('inf')
#                 sums = 0
#                 for i in range(cur,min(n,cur+3)):
#                     sums -= stoneValue[i]
#                     ans = min(ans,sums+score(i+1,True))
#                 return ans
            
#         n = len(stoneValue)
#         res = score(0,True)
#         if res > 0:
#             return "Alice"
#         elif res == 0:
#             return "Tie"
#         else:
#             return "Bob"

# from functools import lru_cache
# class Solution:
#     def stoneGameIII(self, stoneValue: List[int]) -> str:
#         @lru_cache(None)
#         def dfs(start):
#             if start >= len(stoneValue):
#                 return 0
            
            
#             res = float('-inf') 
#             score = 0
            
#             for i in range(start, min(len(stoneValue), start + 3)):
#                 score += stoneValue[i]
#                 res = max(res, score - dfs(i + 1))
            
#             return res
        
#         score = dfs(0)  
#         return 'Tie' if score == 0 else 'Alice' if score > 0 else 'Bob'


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [-float('inf')]*n + [0]
        for i in range(n):
            i = n-i
            sums = 0
            for k in range(max(0,i-3),i)[::-1]:
                sums += stoneValue[k]
                dp[k] = max(dp[k],sums-dp[i])
        score = dp[0]
        return 'Tie' if score == 0 else 'Alice' if score > 0 else 'Bob'