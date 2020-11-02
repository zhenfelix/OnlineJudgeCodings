# class Solution:
#     def maxChunksToSorted(self, arr: List[int]) -> int:
#         nums = sorted(arr)
#         n = len(nums)
#         mp = {}
#         for i in range(n)[::-1]:
#             mp[nums[i]] = i 
#         res, reach = 0, -1
#         for i, a in enumerate(arr):
#             if i > reach:
#                 res += 1
#             reach = max(reach,mp[a])
#             mp[a] += 1
#         return res 


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
