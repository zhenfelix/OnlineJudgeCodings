# import functools
# class Solution:
#     def __init__(self):
#         self.coins = [1,5,10,25]
#     @functools.lru_cache(None)
#     def waysToChange(self, n: int, idx = 0) -> int:
#         if n < 0: return 0
#         if n == 0: return 1
#         return sum(self.waysToChange(n-self.coins[i],i) for i in range(idx,4))%(10**9+7)

# class Solution:
  
#     def waysToChange(self, n: int) -> int:
#         coins = [1,5,10,25]
#         Mod = 10**9+7
#         dp = [[0]*4 for _ in range(25)]
#         dp[-1] = [1,1,1,1]
#         for _ in range(n):
#             cur = [0]*5
#             for k in range(4)[::-1]:
#                 cur[k] = (dp[-coins[k]][k] + cur[k+1])%Mod
#             dp.append(cur[:4])
#             dp = dp[1:]
#         return dp[-1][0]



class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7
        coins = [25, 10, 5, 1]

        f = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n + 1):
                f[i] += f[i - coin]
        return f[n] % mod

