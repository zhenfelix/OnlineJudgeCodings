class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            if i + 1 < n:
                dp[i+1][i] = True
        for k in range(1,n):
            for i in range(n-k):
                dp[i][i+k] = dp[i+1][i+k-1]&(s[i]==s[i+k])

        for i in range(1,n-1):
            for j in range(i+1,n):
                if dp[0][i-1] and dp[i][j-1] and dp[j][n-1]:
                    return True
        return False 
