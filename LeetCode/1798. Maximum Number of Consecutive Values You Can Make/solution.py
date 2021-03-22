class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        cnt = 0
        for cur in sorted(coins):
            if cur > cnt + 1:
                break
            cnt += cur
        return cnt + 1