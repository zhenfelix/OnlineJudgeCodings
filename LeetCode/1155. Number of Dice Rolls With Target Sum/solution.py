class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > f*d:
            return 0
        Mod = 10**9 + 7 
        dp = [[0]*(f*d+1) for _ in range(2)]
        dp[-1][-1] = 1
        for i in range(d):
            idx = i&1
            for j in range(min(f*i+f,target)):
                if j < i:
                    dp[idx][j] = 0
                    continue
                dp[idx][j] = dp[idx][j-1] + dp[1-idx][j-1]
                if j - f - 1 >= 0:
                    dp[idx][j] -= dp[1-idx][j-f-1]
                dp[idx][j] %= Mod
        return dp[(d-1)&1][target-1]


# class Solution:
#     def numRollsToTarget(self, d: int, f: int, target: int) -> int:
#         if target > f*d:
#             return 0
#         M = (10**9) + 7
#         dp = [0]*(f*d+1)
#         for i in range(1,f+1,1):
#             dp[i] = 1
#         for i in range(d-1):
#             new_dp = [0]*(f*d+1)
#             for j in range(1,f*d+1):
#                 for delta in range(1,f+1,1):
#                     if j+delta <= f*d:
#                         new_dp[j+delta] += dp[j]
#                         new_dp[j+delta] %= M
#             dp = new_dp
#         return dp[target]