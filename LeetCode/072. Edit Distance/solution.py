# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         n1, n2 = len(word1), len(word2)
#         dp = [[float('inf')]*(n2+1) for _ in range(n1+1)]
#         for i in range(n1+1):
#             dp[i][0] = i
#         for j in range(n2+1):
#             dp[0][j] = j
#         for i in range(1,n1+1):
#             for j in range(1,n2+1):
#                 dp[i][j] = min(dp[i][j],dp[i][j-1]+1,dp[i-1][j]+1)
#                 if word1[i-1] == word2[j-1]:
#                     dp[i][j] = min(dp[i][j],dp[i-1][j-1])
#                 else:
#                     dp[i][j] = min(dp[i][j],dp[i-1][j-1]+1)
#         return dp[-1][-1]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
        for i in range(len(dp)):
            dp[i][0] = i
        for j in range(len(dp[0])):
            dp[0][j] = j
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = min(dp[i-1][j-1] + (1 if word1[i-1] != word2[j-1] else 0), 1 + dp[i-1][j], 1 + dp[i][j-1])
        return dp[len(word1)][len(word2)]