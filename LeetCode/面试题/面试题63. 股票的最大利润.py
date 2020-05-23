class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, minbuy = 0, float('inf')
        for p in prices:
            minbuy = min(minbuy,p)
            res = max(res, p-minbuy)
        return res