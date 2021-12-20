class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        cnt = 0
        left = 0
        for right in range(n):
            if prices[right]-prices[left] == left-right:
                cnt += right-left+1
            else:
                cnt += 1
                left = right
        return cnt 