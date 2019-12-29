# from functools import lru_cache
# class Solution:
#     def kInversePairs(self, N: int, K: int) -> int:
#         @lru_cache(None)
#         def dfs(n,k):
#             if k == 0:
#                 return 1
#             if k < 0:
#                 return 0
#             if n == 1:
#                 return 0
#             return sum(dfs(n-1,k-(n-i)) for i in range(1,n+1))

#         return dfs(N,K)%(10**9+7)


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [1]+[0]*k
        for i in range(2,n+1):
            presum = dp.copy()
            for j in range(1,k+1):
                presum[j] += presum[j-1]
            for j in range(1,k+1):
                dp[j] = presum[j]-(presum[j-i] if j-i >= 0 else 0)
        return dp[-1]%(10**9+7)
