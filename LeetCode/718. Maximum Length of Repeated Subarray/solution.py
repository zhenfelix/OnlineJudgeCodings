# class Solution:
#     def findLength(self, A: List[int], B: List[int]) -> int:
#         res = 0
#         for i, a in enumerate(A):
#             for j, b in enumerate(B):
#                 k = 0
#                 while i+k < len(A) and j+k < len(B) and A[i+k] == B[j+k]:
#                     k += 1
#                 res = max(res,k)
#         return res

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        res = 0
        n, m = len(A), len(B)
        dp = [0]*(m+1)
        for i in range(n):
            for j in range(1,m+1)[::-1]:
                dp[j] = dp[j-1]+1 if A[i] == B[j-1] else 0
                res = max(res,dp[j])
            # print(dp)
        return res