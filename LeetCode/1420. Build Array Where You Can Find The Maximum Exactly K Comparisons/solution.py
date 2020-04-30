from functools import lru_cache
class Solution(object):
    def numOfArrays(self, N, M, K):
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(i=0, m=-1, rem=K):
            if i == N:
                return +(rem == 0)
            if rem < 0:
                return 0

            ans = 0
            for a in range(1, M + 1):
                if a > m: #newmax
                    ans += dp(i+1, a, rem - 1)
                    ans %= MOD
                else:
                    ans += dp(i+1, m, rem)
                    ans %= MOD
            return ans

        return dp()

DP.  dp(i, m, rem) means that you have to write the array arr[i:] where we had a max of m = max(a[:i]) and 
require a search cost of rem.

# from functools import lru_cache
# class Solution:
#     def numOfArrays(self, N: int, M: int, K: int) -> int:
#         @lru_cache(None)
#         def dfs(m,n,k):
#             if n == 0:
#                 if k == 0:
#                     return 1
#                 else:
#                     return 0
#             if m < 1 or k < 0:
#                 return 0
#             sums = 0
#             for x in range(1,m+1):
#                 sums += dfs(x-1,n-1,k-1)
#                 sums += dfs(m,n-1,k)-dfs(x-1,n-1,k)
#             return sums%(10**9+7)
#         return dfs(M,N,K)