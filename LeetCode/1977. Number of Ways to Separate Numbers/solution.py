class Solution:
    def numberOfCombinations(self, s: str) -> int:
        MOD = 10**9+7
        if s[0] == '0':
            return 0
        n = len(s)
        s += '0'
        reach = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1):
            j = n-1
            while i >= 0:
                if s[i] == s[j]:
                    reach[i][j] = reach[i+1][j+1]+1
                i -= 1
                j -= 1
        # print(reach)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for j in range(n+1):
            dp[0][j] = 1
        for i in range(1,n+1):
            delta = 0
            if s[i] == '0':
                continue
            for j in range(i+1,n+1):
                dp[i][j] += delta
                if i+i-j >= 0 and (reach[i+i-j][i] >= j-i or s[i+i-j+reach[i+i-j][i]] < s[i+reach[i+i-j][i]]):
                    dp[i][j] += dp[i+i-j][i]
                dp[i][j] %= MOD
                if i >= 0:
                    delta += dp[i+i-j][i]
                    delta %= MOD
        # print(dp)
        return sum(dp[i][n] for i in range(n))%MOD



