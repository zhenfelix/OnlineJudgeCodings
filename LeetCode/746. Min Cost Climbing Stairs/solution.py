class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [float('inf')]*(n+1)
        dp[0], dp[1] = 0, 0
        for i in range(2,n+1):
            dp[i] = min(dp[i],dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        # print(dp)
        return dp[-1]