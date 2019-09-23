class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp0, dp1, dp2 = 0, 0, 0
        for cost in costs:
            dp0, dp1, dp2 = min(dp1, dp2)+cost[0], min(dp0,dp2)+cost[1], min(dp0,dp1)+cost[2]
        return min(dp0, dp1, dp2)