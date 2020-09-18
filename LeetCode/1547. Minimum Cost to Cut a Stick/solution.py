class Solution:
    # def minCost(self, n: int, cuts: List[int]) -> int:
    #     cuts.extend([0, n])  # add 2 fake cuts as the boundary of the first cut
    #     cuts.sort()
    #     @functools.lru_cache(None)
    #     def f(i, j):
    #         if i + 1 >= j: return 0
    #         return cuts[j] - cuts[i] + min((f(i, k) + f(k, j) for k in range(i+1, j)), default=0)   # cost of the first cut between ith and jth cut 
    #     # go through all the cuts as the first cut
    #     return f(0, len(cuts)-1)        
    
    def minCost(self, n, A):
        A = sorted(A + [0, n])
        k = len(A)
        dp = [[0] * k for _ in range(k)]
        for d in range(2, k):
            for i in range(k - d):
                dp[i][i + d] = min(dp[i][m] + dp[m][i + d] for m in range(i + 1, i + d)) + A[i + d] - A[i]
        return dp[0][k - 1]

from functools import lru_cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,j):
            res = float('inf')
            for c in cuts:
                if i < c < j:
                    res = min(res, j-i+dfs(i,c)+dfs(c,j))
            if res == float('inf'):
                res = 0
            # print(i,j,res)
            return res
        return dfs(0,n)