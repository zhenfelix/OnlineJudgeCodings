class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort(reverse = True)
        res = 0
        for i in range(0,n,3):
            res += cost[i]
            if i+1 < n:
                res += cost[i+1]
        return res