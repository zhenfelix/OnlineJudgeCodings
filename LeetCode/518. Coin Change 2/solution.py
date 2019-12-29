# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         memo = {}
#         def dfs(idx, w):
#             if (idx,w) in memo:
#                 return memo[idx,w]
#             if w == 0:
#                 memo[idx,w] = 1
                
#             elif idx < 0 or w < 0:
#                 return 0
            
#             else:
#                 memo[idx, w] = dfs(idx, w-coins[idx])+dfs(idx-1, w)
#             return memo[idx, w]
        
#         ans = dfs(len(coins)-1, amount)
#         # print(memo)
#         return ans

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for i in range(len(coins)):
            for w in range(coins[i], amount+1):
                dp[w] += dp[w-coins[i]]
        return dp[-1]


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp = [1]+[0]*amount
#         for i in range(1,amount+1):
#             for coin in coins:
#                 dp[i] += dp[i-coin] if i-coin >= 0 else 0
#         return dp[-1]
# incorrect solution due to duplicate combinations


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1]+[0]*amount
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]