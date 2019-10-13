# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         res, cc, flag = 0, 0, None
#         for ch in s:
#             if cc == 0 or flag == ch:
#                 cc += 1
#                 flag = ch
#             else:
#                 cc -= 1
#             if cc == 0:
#                 res += 1
#         return res

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res, cc = 0, 0
        for ch in s:
            if ch == 'L':
                cc += 1
            else:
                cc -= 1
            if cc == 0:
                res += 1
        return res