class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n, m = len(A), len(A[0])
        dp = [1]*m 
        res = 1
        for j in range(m):
            k = j-1
            while k >= 0:
                if all(A[i][k] <= A[i][j] for i in range(n)):
                # if all([A[i][k] <= A[i][j] for i in range(n)]):
                    dp[j] = max(dp[j], dp[k]+1)
                k -= 1
            res = max(res, dp[j])
        # print(dp)
        return m-res
    
# class Solution:    
#     def minDeletionSize(self, A):
#         n = len(A[0])
#         dp = [1] * n
#         for j in range(1, n):
#             for i in range(j):
#                 if all(s[i] <= s[j] for s in A):
#                     dp[j] = max(dp[j], dp[i] + 1)
#         return n - max(dp)
    
    
# class Solution:
#     def minDeletionSize(self, A):
#         n = len(A[0])
#         dp = [1] * n
#         for idx in range(1,n):
#             for i in range(idx):
#                 if all(s[idx] >= s[i] for s in A):
#                     dp[idx] = max(dp[idx], dp[i] + 1)
#         #print(dp)
#         return n-max(dp)