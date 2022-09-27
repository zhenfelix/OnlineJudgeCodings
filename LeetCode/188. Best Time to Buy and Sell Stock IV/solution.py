class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        f = [0]*(n+1)
        g = [-float('inf')]*(n+1)
        for _ in range(k):
            for i in range(n):
                g[i+1] = max(g[i], f[i]-prices[i])
            for i in range(1,n+1):
                f[i] = max(f[i-1], g[i-1]+prices[i-1])
            # print(g,f)
        return max(f)



# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         n = len(prices)
#         k = min(k,n)
#         if k == 0:
#             return 0
#         cash = [0]*(k+1)
#         hold = [-math.inf]*(k+1)
#         for p in prices:
#             for i in range(k,0,-1):
#                 cash[i], hold[i] = max(cash[i],hold[i]+p), max(hold[i],cash[i-1]-p)
#         return max(cash)
# Time Limit Exceeded the last two test case

# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         def maxProfitInfinity(nums):
#             res = 0
#             for i in range(1,n):
#                 res += max(0, nums[i]-nums[i-1])
#             return res
        
#         n = len(prices)
#         # print(n)
#         if n == 0:
#             return 0
#         if k > n//2:
#             return maxProfitInfinity(prices)
#         cash = [0]*n
#         hold = [-math.inf]*n
#         for _ in range(k):
#             pre_cash = cash.copy()
#             pre_hold = hold.copy()
#             cash[0], hold[0] = 0, -prices[0]
#             for i in range(1,n):
#                 cash[i], hold[i] = max(cash[i-1],hold[i-1]+prices[i]), max(hold[i-1],pre_cash[i-1]-prices[i])
#             # if cash == pre_cash and hold == pre_hold:
#             #     break
#             # print(cash)
#             # print(hold)
#         return cash[-1]

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def maxProfitInfinity(nums):
            res = 0
            for i in range(1,n):
                res += max(0, nums[i]-nums[i-1])
            return res        
        n = len(prices)
        if n == 0:
            return 0
        if k > n//2:
            return maxProfitInfinity(prices)
        cash = [0]*(k+1)
        hold = [-math.inf]*(k+1)
        for p in prices:
            for i in range(k,0,-1):
                cash[i], hold[i] = max(cash[i],hold[i]+p), max(hold[i],cash[i-1]-p)
        return cash[-1]


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        f = [[0]*(n+1) for _ in range(k+1)]
        g = [[0]*(n+1) for _ in range(k+1)]
        for j in range(k+1):
            g[j][0] = -float('inf')
        for i in range(n):
            g[0][i+1] = max(g[0][i], -prices[i])
        for kk in range(k):
            for i in range(1, n+1):
                f[kk+1][i] = max(f[kk+1][i-1], prices[i-1]+g[kk][i-1])
                g[kk+1][i] = max(g[kk+1][i-1], f[kk+1][i-1]-prices[i-1])
        return f[-1][-1]