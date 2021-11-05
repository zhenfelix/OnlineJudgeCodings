class Solution:
    def canPartition(self, stones: List[int]) -> bool:
        tot = sum(stones)
        if tot%2:
            return False
        target = tot//2
        dp = [0]*(target+1)
        dp[0] = 1
        for x in stones:
            for t in range(target, x-1, -1):
                dp[t] |= dp[t-x]
        return dp[-1] == 1
