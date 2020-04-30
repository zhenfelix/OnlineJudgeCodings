# from functools import lru_cache
# import sys 

# class Solution:
#     def numberOfArrays(self, s: str, k: int) -> int:
#         sys.setrecursionlimit(10**6) 
#         n = len(s)
#         @lru_cache(None)
#         def dfs(cur):
#             if cur >= n:
#                 return 1
#             if s[cur] == '0':
#                 return 0
#             sums = 0
#             for i in range(cur+1,n+1):
#                 num = int(s[cur:i])
#                 if num > k:
#                     break
#                 sums += dfs(i)
#             return sums%(10**9+7)
#         return dfs(0)


class Solution(object):
    def numberOfArrays(self, s, k):
        MOD = 10**9 + 7
        n = len(s)
        klen = len(str(k))
        dp = [0] * (n + 1)  # dp[i]: number of ways to write s[i:]
        dp[n] = 1
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':  # number cant start with or be 0
                continue
            cur = 0  # cur: int(s[i..j])
            for j in range(i, min(i + klen, n)):
                cur = 10 * cur + int(s[j])
                if cur > k:
                    break
                # We can write `cur` first, then have dp[j + 1] ways
                dp[i] = (dp[i] + dp[j + 1]) % MOD
        return dp[0]