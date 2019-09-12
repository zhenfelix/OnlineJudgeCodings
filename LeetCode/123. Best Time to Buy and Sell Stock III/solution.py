class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash0, hold0 = 0, -math.inf
        cash1, hold1 = 0, -math.inf
        cash2, hold2 = 0, -math.inf
        for p in prices:
            cash2, hold2 = max(cash2, hold2+p), max(hold2, cash1-p)
            cash1, hold1 = max(cash1, hold1+p), max(hold1, cash0-p)
        return cash2