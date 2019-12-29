# from functools import lru_cache
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         @lru_cache(None)
#         def dfs(idx, total):
#             if total == 0:
#                 return 0
#             if total < 0 or idx < 0:
#                 return float("inf")
#             return min(1+dfs(idx,total-coins[idx]),dfs(idx-1,total))
#         coins.sort()
#         res = dfs(len(coins)-1,amount)
#         return res if res != float("inf") else -1

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [0] + [float("inf")]*amount
#         for i in range(1,1+amount):
#             for coin in coins:
#                 dp[i] = min(dp[i],(dp[i-coin]+1 if i-coin >= 0 else float("inf")))
#         return dp[-1] if dp[-1] < float("inf") else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")]*amount
        for coin in coins:
            for i in range(coin,1+amount):
                dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[-1] if dp[-1] < float("inf") else -1