# from functools import lru_cache
# class Solution:
#     def minStickers(self, stickers: List[str], target: str) -> int:
#         n = len(stickers)
#         mp = [Counter(stickers[i]) for i in range(n)]
#         # for ch in set(target):
#         #     if all(mp[i][ch] == 0 for i in range(n)):
#         #         return -1


#         def helper(x,cc):
#             cntx = Counter(x)
#             tmp  = []
#             for k, v in cntx.items():
#                 v -= cc[k]
#                 if v > 0:
#                     tmp.append(k*v)
#             return ''.join(sorted(tmp))

#         @lru_cache(None)
#         def dfs(s):
#             if not s:
#                 return 0
#             res = float('inf')
#             for i in range(n):
#                 nxt = helper(s,mp[i])
#                 if nxt == s:
#                     continue
#                 res = min(res, dfs(nxt))
#             return res + 1

#         ans = dfs(''.join(sorted(target)))
#         return -1 if ans == float('inf') else ans

from functools import lru_cache
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(stickers)
        mp = [Counter(stickers[i]) for i in range(n)]

        @lru_cache(None)
        def dfs(cur):
            if not cur:
                return 0
            res = float('inf')
            for i in range(n):
                if mp[i][cur[0]] == 0:
                    continue
                nxt = ''
                cc = Counter(cur)
                for ch in range(26):
                    ch = chr(ord('a') + ch)
                    cc[ch] -= mp[i][ch]
                    if cc[ch] > 0:
                        nxt += ch*cc[ch]
                res = min(res, dfs(nxt))
            return res + 1

        ans = dfs(''.join(sorted(target)))
        return -1 if ans == float('inf') else ans