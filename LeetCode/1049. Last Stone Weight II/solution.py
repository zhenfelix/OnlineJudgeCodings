class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot = sum(stones)
        target = tot//2
        dp = [0]*(target+1)
        dp[0] = 1
        for x in stones:
            for t in range(target, x-1, -1):
                dp[t] |= dp[t-x]
        for t in range(target,-1,-1):
            if dp[t]:
                return tot-t-t
        return -1
