import math

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#         lo = math.inf
#         for hi in prices:
#             lo = min(lo, hi)
#             res = max(res, hi-lo)
#         return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash, hold = 0, -math.inf
        for p in prices:
            cash = max(cash, hold+p)
            hold = max(hold, -p)
        return cash
    
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/most-consistent-ways-of-dealing-with-the-series-of-stock-problems

