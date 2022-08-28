# class Solution:
#     def maxChunksToSorted(self, arr: List[int]) -> int:
#         mp = dict()
#         for i, x in enumerate(sorted(arr)):
#             if x not in mp:
#                 mp[x] = i 
#         reach = -1
#         cnt = 0
#         for i, x in enumerate(arr):
#             reach = max(reach, mp[x])
#             mp[x] += 1
#             if i == reach:
#                 cnt += 1
#         return cnt


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mi = arr[:] + [float('inf')]
        n = len(arr)
        for i in range(n)[::-1]:
            mi[i] = min(mi[i],mi[i+1])
        cur, res = 0, 0
        for i, a in enumerate(arr):
            cur = max(cur,a)
            if cur <= mi[i+1]:
                res += 1
        return res 
