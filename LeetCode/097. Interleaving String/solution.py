class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n+m != len(s3):
            return False
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True
        for k in range(n+m):
            for i in range(max(0,k-m), min(n+1,k+1)):
                j = k-i
                if dp[i][j]:
                    if i+1 <= n and s1[i] == s3[k]:
                        dp[i+1][j] = True
                    if j+1 <= m and s2[j] == s3[k]:
                        dp[i][j+1] = True
        return dp[-1][-1]

