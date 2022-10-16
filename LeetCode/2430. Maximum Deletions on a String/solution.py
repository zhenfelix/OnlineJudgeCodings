class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        same = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1)[::-1]:
            j = n-1
            while i >= 0:
                if s[i] == s[j]:
                    same[i][j] = 1 + same[i+1][j+1]
                i -= 1
                j -= 1
        # print(same)
        dp = [1]*n 
        for i in range(n)[::-1]:
            for j in range(i+1,n):
                if same[i][j] >= j-i:
                    dp[i] = max(dp[i], dp[j]+1)
        return dp[0]





class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1)[::-1]:
            j = n-1
            while i >= 0:
                if s[i] == s[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                i -= 1
                j -= 1
        # print(dp)

        @lru_cache(None)
        def dfs(i):
            ans = 1
            for j in range(i+1,n):
                if dp[i][j] >= j-i:
                    ans = max(ans, dfs(j)+1)
            return ans 
        return dfs(0)