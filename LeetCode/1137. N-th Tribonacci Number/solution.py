# class Solution:
#     def tribonacci(self, n: int) -> int:
#         memo = {0:0,1:1,2:1}
#         def dp(x):
#             if x in memo:
#                 return memo[x]
#             memo[x] = dp(x-1)+dp(x-2)+dp(x-3)
#             return memo[x]
#         return dp(n)

class Solution:
    def tribonacci(self, n):
        a, b, c = 1, 0, 0
        for _ in range(n): a, b, c = b, c, a + b + c
        return c