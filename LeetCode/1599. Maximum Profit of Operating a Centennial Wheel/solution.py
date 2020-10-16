class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost*4 <= runningCost:
            return -1
        ans, res, sums, waiting, step = -1, -float('inf'), 0, 0, 0
        while waiting or step < len(customers):
            if step < len(customers):
                waiting += customers[step]
            if waiting >= 4:
                sums += boardingCost*4 - runningCost
                waiting -= 4
            else:
                sums += boardingCost*waiting - runningCost
                waiting = 0
            step += 1
            if sums > res:
                res = sums
                ans = step
        return ans if res > 0 else -1