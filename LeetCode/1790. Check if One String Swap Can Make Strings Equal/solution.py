class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = [[x, y] for x, y in zip(s1, s2) if x != y]
        return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]

# class Solution:
#     def areAlmostEqual(self, s1: str, s2: str) -> bool:
#         left, right = [], []
#         n = len(s1)
#         for i in range(n):
#             if s1[i] != s2[i]:
#                 left.append(s1[i])
#                 right.append(s2[i])
#             if len(left) > 2:
#                 return False
#         if len(left)%2 == 0:
#             return left == right[::-1]
#         return False