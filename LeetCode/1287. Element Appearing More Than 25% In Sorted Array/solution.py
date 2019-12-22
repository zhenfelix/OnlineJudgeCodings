class Solution(object):
    def findSpecialInteger(self, arr):
        if len(arr) < 4:
            return arr[0]
        size = (len(arr)) // 4
        # loose = max(1, size)
        for index in range(0, len(arr), size):
            candidate = arr[index]
            left = bisect.bisect_left(arr, candidate)
            right = bisect.bisect_right(arr, candidate)
            if right - left > size:
                return arr[index]
        assert(False)


# class Solution:
#     def findSpecialInteger(self, arr: List[int]) -> int:
#         n = len(arr)
#         cnt = 0
#         cur = -1
#         for a in arr:
#             if a != cur:
#                 cur = a
#                 cnt = 1
#             else:
#                 cnt += 1
#             if cnt > n/4:
#                 return cur


# from collections import Counter
# class Solution:
#     def findSpecialInteger(self, arr):
#         return Counter(arr).most_common(1)[0][0]