# from functools import lru_cache
# import bisect
# class Solution:
#     def distinctSubseqII(self, S: str) -> int:
#         MOD = 10**9+7
#         mp = defaultdict(deque)
#         for i, ch in enumerate(S):
#             mp[ch].append(i)
#         n = len(S)
#         mp[chr(ord('a')+26)].append(n)
#         @lru_cache(None)
#         def dfs(idx):
#             if idx >= n:
#                 return 1
#             res = 0
#             for i in range(27):
#                 ch = chr(ord('a')+i)
#                 nxt = bisect.bisect_left(mp[ch],idx)
#                 if nxt < len(mp[ch]):
#                     res += dfs(mp[ch][nxt]+1)
#             # print(idx,res)
#             return res%MOD
#         return dfs(0)-1

# from functools import lru_cache
# class Solution:
#     def distinctSubseqII(self, S: str) -> int:
#         MOD = 10**9+7
#         mp = defaultdict(deque)
#         for i, ch in enumerate(S):
#             mp[ch].append(i)
#         n = len(S)
#         mp[chr(ord('a')+26)].append(n)
#         pos = defaultdict(int)
#         for i in range(27):
#             for j in range(n):
#                 ch = chr(ord('a')+i)
#                 if not mp[ch]:
#                     pos[ch,j] = -1
#                     continue
#                 pos[ch,j] = mp[ch][0]
#                 if j == mp[ch][0]:
#                     mp[ch].popleft()
#         @lru_cache(None)
#         def dfs(idx):
#             if idx >= n:
#                 return 1
#             res = 0
#             for i in range(27):
#                 ch = chr(ord('a')+i)
#                 nxt = pos[ch,idx]
#                 if nxt >= 0:
#                     res += dfs(nxt+1)
#             # print(idx,res)
#             return res%MOD
#         return dfs(0)-1

class Solution:
    def distinctSubseqII(self, S):
        end = [0] * 26
        for c in S:
            end[ord(c) - ord('a')] = sum(end) + 1
        return sum(end) % (10**9 + 7)


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9+7
        cc = Counter()
        for ch in s:
            cc[ch] = (sum(cc.values())+1)%MOD
        return sum(cc.values())%MOD