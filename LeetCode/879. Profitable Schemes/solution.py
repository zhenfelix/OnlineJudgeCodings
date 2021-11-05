# from functools import lru_cache
# class Solution:
#     def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
#         MOD = 10**9+7
#         n = len(profit)
#         psum = profit + [0]
#         for i in range(n)[::-1]:
#             psum[i] += psum[i+1]
#         # print(psum)
#         @lru_cache(None)
#         def dfs(g, p, idx):
#             # if g < 0:
#             #     return 0
#             # if idx == n:
#             #     return 1 if p <= 0 else 0
#             if g < 0 or p > psum[idx]:
#                 return 0
#             if idx == n:
#                 return 1
#             p = max(p,0)
#             res = (dfs(g, p, idx+1) + dfs(g-group[idx], p-profit[idx], idx+1))%MOD
#             # print(g,p,idx,res)
#             return res
#         return dfs(G,P,0)


# class Solution:
#     def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
#         m = len(group)
#         MOD = 10**9+7
#         @lru_cache(None)
#         def dfs(i, g, p):
#             if g < 0:
#                 return 0
#             # if p <= 0:
#             #     return pow(2,m-i,MOD)
#             if i == m:
#                 return p <= 0 and g >= 0
#             return (dfs(i+1, g, p) + dfs(i+1, g-group[i], max(0,p-profit[i])))%MOD
#         return dfs(0, n, minProfit)

# class Solution:
#     def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
#         m = len(group)
#         MOD = 10**9+7
#         @lru_cache(None)
#         def dfs(i, g, p):
#             if g < 0:
#                 return 0
#             # if p <= 0:
#             #     return pow(2,m-i,MOD)
#             if i == m:
#                 return p <= 0 and g >= 0
#             return (dfs(i+1, g, p) + dfs(i+1, g-group[i], max(0,p-profit[i])))%MOD
#         return dfs(0, n, minProfit)


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        MOD = 10**9+7
        dp = [[0]*(minProfit+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(m):
            for g in range(n+1)[::-1]:
                for p in range(minProfit+1)[::-1]:
                    if g-group[i] >= 0:
                        dp[g][p] += dp[g-group[i]][max(0,p-profit[i])]
                        dp[g][p] %= MOD

        return dp[-1][-1]