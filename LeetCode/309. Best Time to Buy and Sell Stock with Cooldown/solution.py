# import math

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         if n == 0:
#             return 0
#         cash, hold = [0]*n, [-prices[0]]*n
#         for i in range(1,n):
#             cash[i] = max(cash[i-1], hold[i-1]+prices[i])
            
#             if i-2 >= 0:
#                 hold[i] = max(hold[i-1], cash[i-2]-prices[i])
#             else:
#                 hold[i] = max(hold[i-1], -prices[i])
#         # print(cash)
#         # print(hold)
#         return cash[-1]
        
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash, hold, cool = 0, -math.inf, 0
        for p in prices:
            hold, cash, cool = max(hold,cool-p), hold+p, max(cool, cash)
        return max(cash,cool)
        