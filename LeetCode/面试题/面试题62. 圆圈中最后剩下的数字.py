# import sys
# sys.setrecursionlimit(10**6)
# class Solution:
#     def lastRemaining(self, n: int, m: int) -> int:
#         if n == 1:
#             return 0
#         return (m%n + self.lastRemaining(n-1,m))%n


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        for i in range(2,n+1):
            res += m%i 
            res %= i 
        return res