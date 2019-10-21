# class Solution:
#     def nthPersonGetsNthSeat(self, n: int) -> float:
#         def dfs(x):
#             if x in memo:
#                 return memo[x]
#             if x == 1:
#                 memo[x] = 1
#                 return 1
#             res = 1/x
#             for i in range(2,x):
#                 res += (1/x)*dfs(i)
#             memo[x] = res
#             return res
#         memo = {}
#         return dfs(n)

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        return 0.5