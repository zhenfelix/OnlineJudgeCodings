# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n, m = len(text1), len(text2)
#         dp = [0]*(m+1)
#         for i in range(1,n+1,1):
#             tmp = dp.copy()
#             for j in range(1,m+1,1):
#                 if text1[i-1] == text2[j-1]:
#                     dp[j] = max(tmp[j],tmp[j-1]+1,dp[j-1])
#                 else:
#                     dp[j] = max(tmp[j],tmp[j-1],dp[j-1])
#         return dp[-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [0]*(n2+1)
        for i in range(1,n1+1):
            cur = 0
            for j in range(1,n2+1):
                pre, cur = cur, dp[j]
                dp[j] = max(dp[j],dp[j-1],pre+(text1[i-1]==text2[j-1]))
        return dp[-1]