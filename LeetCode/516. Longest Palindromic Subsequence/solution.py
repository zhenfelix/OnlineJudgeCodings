# from functools import lru_cache
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         @lru_cache(None)
#         def dfs(i,j):
#             if i > j:
#                 return j-i+1
#             for k in range(i,j+1):
#                 if s[k] == s[j]:
#                     return max(dfs(i,j-1),2+dfs(k+1,j-1))
#             return -1
#         return dfs(0,n-1)
#         

# from functools import lru_cache
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         @lru_cache(None)
#         def dfs(i,j):
#             if i > j:
#                 return j-i+1
#             res = max(dfs(i,j-1),dfs(i+1,j))
#             if s[i] == s[j]:
#                 res = max(res, 2+dfs(i+1,j-1))
#             return res
#         return dfs(0,n-1)
#         


# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         if n == 1:
#             return 1
#         dp = [[1]*n for _ in range(n)]
#         for i in range(1,n):
#             if s[i] == s[i-1]:
#                 dp[i-1][i] = 2
#         for sz in range(3,n+1):
#             for j in range(2,n):
#                 i = j - sz + 1
#                 dp[i][j] = max(dp[i+1][j],dp[i][j-1])
#                 if s[i] == s[j]:
#                     dp[i][j] = max(dp[i][j], 2+dp[i+1][j-1])
#         return dp[0][n-1]
  

# class Solution(object):
#     def longestPalindromeSubseq(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         n = len(s)
#         dp = [[1] * 2 for _ in range(n)]
#         for j in range(1, len(s)):
#             for i in reversed(range(0, j)):
#                 if s[i] == s[j]:
#                     dp[i][j%2] = 2 + dp[i + 1][(j - 1)%2] if i + 1 <= j - 1 else 2
#                 else:
#                     dp[i][j%2] = max(dp[i + 1][j%2], dp[i][(j - 1)%2])
#         return dp[0][(n-1)%2]

# class Solution(object):
#     def longestPalindromeSubseq(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         n = len(s)
#         dp = [[0] * 2 for _ in range(n)]
#         for i in range(n):
#             dp[i][i%2] = 1
#         for j in range(1, len(s)):
#             for i in reversed(range(0, j)):
#                 if s[i] == s[j]:
#                     dp[i][j%2] = 2 + dp[i + 1][(j - 1)%2]
#                 else:
#                     dp[i][j%2] = max(dp[i + 1][j%2], dp[i][(j - 1)%2])
#         return dp[0][(n-1)%2]

class Solution:
    def longestPalindromeSubseq(self, s):
        # if s == s[::-1]:
        #     return len(s)

        n = len(s)
        dp = [0 for j in range(n)]
        dp[n-1] = 1

        for i in range(n-1, -1, -1):   # can actually start with n-2...
            newdp = dp[:]
            newdp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j-1]
                else:
                    newdp[j] = max(dp[j], newdp[j-1])
            dp = newdp
                    
        return dp[n-1]


# class Solution:
#     def longestPalindromeSubseq(self, s):
#         n = len(s)
#         dp = [[0]*(n+1) for _ in range(n+1)]
#         for i in range(n)[::-1]:
#             pos = {}
#             for j in range(i,n):
#                 if s[j] not in pos:
#                     pos[s[j]] = j 
#                 left, right = pos[s[j]]+1, j-1
#                 dp[i][j] = max(dp[i][j-1],dp[left][right]+2+min(right-left+1,0))
#         return dp[0][n-1]