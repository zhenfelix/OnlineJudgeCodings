# from functools import lru_cache
# class Solution:
#     def countPalindromicSubsequences(self, S: str) -> int:
#         @lru_cache(None)
#         def dfs(i,j):
#             if i > j:
#                 return 1
#             res = 1
#             for ch in "abcd":
#                 lo, hi = i, j
#                 while lo <= j and S[lo] != ch:
#                     lo += 1
#                 while hi >= i and S[hi] != ch:
#                     hi -= 1
#                 if lo <= hi:
#                     res += dfs(lo+1,hi-1) + (lo<hi)
#             return res%(10**9+7)
#         return dfs(0,len(S)-1) - 1

from functools import lru_cache
class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        nxt = collections.defaultdict(int)
        pre = collections.defaultdict(int)
        n = len(S)
        for i in range(n)[::-1]:
            for ch in "abcd":
                nxt[ch,i] = i if ch == S[i] else nxt.get((ch,i+1),n)
        for i in range(n):
            for ch in "abcd":
                pre[ch,i] = i if ch == S[i] else pre.get((ch,i-1),-1)
        @lru_cache(None)
        def dfs(i,j):
            if i > j:
                return 1
            res = 1
            for ch in "abcd":
                lo, hi = nxt[ch,i], pre[ch,j]
                if lo <= hi:
                    res += dfs(lo+1,hi-1) + (lo<hi)
            return res%(10**9+7)
        return dfs(0,len(S)-1) - 1