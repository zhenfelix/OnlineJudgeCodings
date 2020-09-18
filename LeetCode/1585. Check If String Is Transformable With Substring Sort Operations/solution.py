# import bisect
# class Solution:
#     def isTransformable(self, s: str, t: str) -> bool:
#         mp = defaultdict(deque)
#         for i, ch in enumerate(s):
#             mp[int(ch)].append(i)
#         for ch in t:
#             if len(mp[int(ch)]) == 0:
#                 return False
#             cur = mp[int(ch)].popleft()
#             for k in range(int(ch)):
#                 idx = bisect.bisect_left(mp[k],cur)
#                 if len(mp[k]) and idx > 0:
#                     return False
#         return True

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        mp = defaultdict(deque)
        for i, ch in enumerate(s):
            mp[int(ch)].append(i)
        for ch in t:
            if len(mp[int(ch)]) == 0:
                return False
            cur = mp[int(ch)].popleft()
            for k in range(int(ch)):
                if len(mp[k]) and mp[k][0] < cur:
                    return False
        return True