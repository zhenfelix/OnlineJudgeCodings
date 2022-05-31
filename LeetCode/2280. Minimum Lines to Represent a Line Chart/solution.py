class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        stockPrices.sort()
        ans = 1
        if n < 3:
            return ans if n == 2 else 0
        for i in range(2,n):
            d1, d2 = stockPrices[i][0]-stockPrices[i-1][0], stockPrices[i-1][0]-stockPrices[i-2][0]
            p1, p2 = stockPrices[i][1]-stockPrices[i-1][1], stockPrices[i-1][1]-stockPrices[i-2][1]
            if p1*d2 != p2*d1:
                ans += 1 
        return ans