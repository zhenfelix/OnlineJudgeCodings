# from functools import lru_cache
# class Solution:
#     def numWays(self, words: List[str], target: str) -> int:
#         mp = defaultdict(int)
#         MOD = 10**9+7
#         n, m = len(target), len(words[0])
#         for word in words:
#             for i, w in enumerate(word):
#                 mp[w,i] += 1

#         @lru_cache(None)
#         def dfs(t,k):
#             if t == n:
#                 return 1
#             if k == m:
#                 return 0
#             return sum([mp[target[t],j]*dfs(t+1,j+1) for j in range(k,m) if mp[target[t],j] > 0])%MOD
#         return dfs(0,0)



from functools import lru_cache
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mp = defaultdict(int)
        MOD = 10**9+7
        n, m = len(target), len(words[0])
        for word in words:
            for i, w in enumerate(word):
                mp[w,i] += 1

        @lru_cache(None)
        def dfs(t,k):
            if t == n:
                return 1
            if k == m:
                return 0
            res = dfs(t,k+1)
            if mp[target[t],k] > 0:
                res += mp[target[t],k]*dfs(t+1,k+1)
            return res%MOD
            # return (dfs(t,k+1) + mp[target[t],k]*dfs(t+1,k+1))%MOD
            # return sum([mp[target[t],j]*dfs(t+1,j+1) for j in range(k,m) if mp[target[t],j] > 0])%MOD
        return dfs(0,0)


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mp = defaultdict(int)
        MOD = 10**9+7
        n, m = len(target), len(words[0])
        for word in words:
            for i, w in enumerate(word):
                mp[w,i] += 1

        dp = [0]*(n+1)
        dp[-1] = 1
        for k in range(m)[::-1]:
            for t in range(n):
                dp[t] += dp[t+1]*mp[target[t],k]
        return dp[0]%MOD