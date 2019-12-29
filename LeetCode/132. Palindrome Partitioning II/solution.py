# from functools import lru_cache
# class Solution:
#     def minCut(self, s: str) -> int:
#         @lru_cache(None)
#         def dfs(i,j):
#             if s[i:j+1] == s[i:j+1][::-1]:
#                 return 0
#             return min(dfs(i,k)+dfs(k+1,j)+1 for k in range(i,j))
#         return dfs(0,len(s)-1)


# class Solution:
#     def minCut(self, s: str) -> int:
#         n = len(s)
#         pair = [[False]*n for _ in range(n)]
#         pair[0][0] = True
#         for i in range(1,n):
#             pair[i][i] = True
#             pair[i][i-1] = True
#         for j in range(1,n):
#             for i in range(0,j)[::-1]:
#                 if pair[i+1][j-1] and s[i] == s[j]:
#                     pair[i][j] = True
#         # print(pair)
#         dp = [i for i in range(n)]
#         for i in range(1,n):
#             if pair[0][i]:
#                 dp[i] = 0
#             else:
#                 dp[i] = min(dp[k]+1 for k in range(i) if pair[k+1][i])
#         return dp[-1]

# class Solution:
#     def minCut(self, s: str) -> int:
#         n = len(s)
#         pair = [[False]*n for _ in range(n)]
#         pair[0][0] = True
#         for i in range(1,n):
#             pair[i][i] = True
#             pair[i][i-1] = True
       
#         dp = [i for i in range(n)]
#         for j in range(1,n):
#             dp[j] = dp[j-1]+1
#             for i in range(j)[::-1]:
#                 if s[i] == s[j] and pair[i+1][j-1]:
#                     if i == 0:
#                         dp[j] = 0
#                     else:
#                         dp[j] = min(dp[j],dp[i-1]+1)
#                     pair[i][j] = True
#         return dp[-1]


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i-1 for i in range(n+1)]
        for i in range(n):
            j = 0
            while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
                dp[i+j+1] = min(dp[i+j+1],dp[i-j]+1)
                j += 1
            j = 1
            while i-j+1 >= 0 and i+j < n and s[i-j+1] == s[i+j]:
                dp[i+j+1] = min(dp[i+j+1],dp[i-j+1]+1)
                j += 1
        return dp[-1]