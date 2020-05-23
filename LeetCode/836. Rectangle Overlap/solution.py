# from functools import lru_cache
# class Solution:
#     def new21Game(self, N: int, K: int, W: int) -> float:
#         @lru_cache(None)
#         def dfs(n,k,w):
#             if k <= 0:
#                 return 1 if n >= 0 else 0
#             return sum(dfs(n-i,k-i,w) for i in range(1,1+w))/w
#         return dfs(N, K, W)


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        p = [1 if N-K-i >= 0 else 0 for i in range(W)][::-1]
        sums = sum(p) 
        for k in range(K):
            p.append(sums/W)
            sums += p[-1]-p[-W-1]
        return p[-1]