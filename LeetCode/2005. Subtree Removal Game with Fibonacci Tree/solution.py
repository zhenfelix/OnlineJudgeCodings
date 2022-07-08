class Solution:
    def findGameWinner(self, n: int) -> bool:
        if n == 1:
            return False
        dp = [0]*n
        dp[1] = 1
        for i in range(n):
            dp[i] = 1+(dp[i-1]^dp[i-2])
        return (dp[i-1]^dp[i-2]) > 0