# class Solution:
#     def numPermsDISequence(self, S: str) -> int:
#         M = 10**9 + 7
#         n = len(S)
#         dp = [1]*(n+1)
#         # print(dp)
#         k = n
#         for ch in S:
            
#             if ch == 'D':
#                 for i in range(k):
#                     dp[i] = sum(dp[i+1:k+1])%M
#             else:
#                 for i in range(k-1,-1,-1):
#                     dp[i] = sum(dp[:i+1])%M
#             # print(dp)
#             k -= 1
#         return dp[0]

class Solution:
#     def numPermsDISequence(self, S: str) -> int:
#         M = 10**9 + 7
#         n = len(S)
#         dp = [1]*(n+1)
#         # print(dp)
#         k = n
#         for ch in S:
            
#             if ch == 'D':
#                 sums = sum(dp[:k+1])
#                 for i in range(k):
#                     sums -= dp[i]
#                     dp[i] = sums
#             else:
#                 for i in range(1,k):
#                     dp[i] += dp[i-1]
#             # print(dp)
#             k -= 1
#         return dp[0]%M
    def numPermsDISequence(self, S):
        dp = [1] * (len(S) + 1)
        for c in S:
            if c == "I":
                dp = dp[:-1]
                for i in range(1, len(dp)):
                    dp[i] += dp[i - 1]
            else:
                dp = dp[1:]
                for i in range(len(dp) - 1)[::-1]:
                    dp[i] += dp[i + 1]
        return dp[0] % (10**9 + 7)