# // TLE O(N2)
# class Solution:
#     def lenLongestFibSubseq(self, arr: List[int]) -> int:
#         dp = defaultdict(int)
#         res = 0
#         n = len(arr)
#         for i in range(n):
#             for j in range(i):
#                 # dp[i][arr[j]] = max(dp[i][arr[j]], 2)
#                 dp[i,arr[j]] = max(dp[i,arr[j]], max(1,dp[j,arr[i]-arr[j]])+1)
#                 if dp[i,arr[j]] >= 3:
#                     res = max(res, dp[i,arr[j]])
#                 # print(i,j,dp[i,arr[j]])
#         return res 

