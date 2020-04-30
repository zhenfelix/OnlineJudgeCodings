# class Solution:
#     def countOrders(self, n: int) -> int:
#         Mod = 10**9+7
#         sums = 1
#         for i in range(2,n+1):
#             sums *= (i*2-1)*i
#             sums %= Mod
#         return sums

from functools import reduce
class Solution:
    def countOrders(self, n: int) -> int:
		# remember to use generator instead of tuple for O(1) space complexity
        return reduce(lambda x, y: x * y % (10**9+7), (v for x in range(1,n+1) for v in (x, 2*x-1)), 1)