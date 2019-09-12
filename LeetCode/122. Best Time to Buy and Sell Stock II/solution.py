import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash, hold = 0, -math.inf
        for p in prices:
            cash, hold = max(cash,hold+p), max(hold,cash-p)
        return cash