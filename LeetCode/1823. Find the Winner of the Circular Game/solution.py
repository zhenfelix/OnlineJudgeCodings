class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         # def dfs(t):
#         #     if t == 1:
#         #         return 1
#         #     return ((k+t)%t+dfs(t-1)-1)%t+1
#         # return dfs(n)

#         dp = 1
#         for t in range(2,n+1):
#             dp += k-1
#             dp %= t 
#             dp += 1
#             # print(t,dp)
#         return dp


    def findTheWinner(self, n, k):
        res = 0
        for i in range(1, n + 1):
            res = (res + k) % i
        return res + 1