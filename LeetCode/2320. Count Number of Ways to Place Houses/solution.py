class Solution:
    def countHousePlacements(self, n: int) -> int:
        if n < 3:
            return (n+1)**2
        MOD = 10**9+7
        dp = [1]*n
        for i in range(n):
            dp[i] = dp[i-1]+dp[i-2]
            dp[i] %= MOD
        # print(dp)
        return (dp[-1]**2)%MOD


class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(idx, last_two):
            if idx == n*2:
                return 1
            ans = 0
            for k in range(2):
                if k == last_two[0] == 1:
                    continue
                ans += dfs(idx+1, (last_two[-1],k))
            return ans%MOD
        return dfs(0,(0,0))


class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(idx, last_two):
            if idx == n*2:
                return 1
            ans = 0
            ans += dfs(idx+1, (last_two[-1],last_two[0]^1))
            if last_two[0] == 0:
                ans += dfs(idx+1, (last_two[-1],last_two[0]))
            return ans%MOD
        return dfs(0,(0,0))


