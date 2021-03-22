# class Solution:
#     def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
#         sell, buy = [], []
#         total, MOD = 0, 10**9+7
#         for price, amount, otype in orders:
#             if otype == 0:
#                 while amount > 0 and sell and sell[0][0] <= price:
#                     p, a = heapq.heappop(sell)
#                     tmp = min(amount,a)
#                     total -= tmp
#                     amount -= tmp
#                     a -= tmp
#                     if a > 0:
#                         heapq.heappush(sell,(p,a))
#                 if amount > 0:
#                     heapq.heappush(buy,(-price,amount))
#                     total += amount
#             else:
#                 while amount > 0 and buy and -buy[0][0] >= price:
#                     p, a = heapq.heappop(buy)
#                     tmp = min(amount,a)
#                     total -= tmp
#                     amount -= tmp
#                     a -= tmp
#                     if a > 0:
#                         heapq.heappush(buy,(p,a))
#                 if amount > 0:
#                     heapq.heappush(sell,(price,amount))
#                     total += amount
#             total %= MOD
#         return total

class Solution:
    def getNumberOfBacklogOrders(self, orders):
        sell, buy = [], []
        for p, a, t in orders:
            if t == 0:
                heapq.heappush(buy, [-p, a])
            else:
                heapq.heappush(sell, [p, a])
            while sell and buy and sell[0][0] <= -buy[0][0]:
                k = min(buy[0][1], sell[0][1])
                buy[0][1] -= k
                sell[0][1] -= k
                if buy[0][1] == 0: heapq.heappop(buy)
                if sell[0][1] == 0: heapq.heappop(sell)
        return sum(a for p, a in buy + sell) % (10**9 + 7)        