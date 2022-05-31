class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = [[0]*3 for _ in range(2)]
        for ch in s:
            cur = int(ch)
            dp[cur][2] += dp[cur][1]
            dp[1-cur][1] += dp[1-cur][0]
            dp[cur][0] += 1
        return dp[0][-1]+dp[1][-1]