class Solution:
    # def minScoreTriangulation(self, A):
    #     memo = {}
    #     def dp(i, j):
    #         if j-i<2:
    #             memo[i,j] = 0
    #         elif (i, j) not in memo:
    #             memo[i, j] = min([dp(i, k) + dp(k, j) + A[i] * A[j] * A[k] for k in range(i + 1, j)])
    #         return memo[i, j]
    #     return dp(0, len(A) - 1)
    
    
    def minScoreTriangulation(self, A):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                memo[i, j] = min([dp(i, k) + dp(k, j) + A[i] * A[j] * A[k] for k in range(i + 1, j)] or [0])
            return memo[i, j]
        return dp(0, len(A) - 1)