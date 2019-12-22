class Solution:
    def removeCoveredIntervals(self, A):
        res = right = 0
        for i, j in sorted(A, key=lambda a: [a[0], -a[1]]):
            res += j > right
            right = max(right, j)
        return res        


# class Solution:
#     def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
#         ans = 0
#         for i, a in enumerate(intervals):
#             flag = True
#             for j, b in enumerate(intervals):
#                 if j == i:
#                     continue
#                 if b[0] <= a[0] and b[1] >= a[1]:
#                     flag = False
#                     break
#             if flag:
#                 ans += 1
#         return ans
#                 