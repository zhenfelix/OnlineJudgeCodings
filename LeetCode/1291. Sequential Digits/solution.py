# class Solution:
#     def sequentialDigits(self, low: int, high: int) -> List[int]:
#         cur, num = 12, 100
#         res = []
#         while cur <= high:
#             if cur >= low:
#                 res.append(cur)
#             # print(cur)
#             if cur%10 < 9:
#                 cur = (cur*10)%num + cur%10+1
#             else:
#                 cur = 1
#                 while cur < num:
#                     cur = cur*10 + cur%10+1
#                 num *= 10
#         return res

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        s = '123456789'
        a = [int(s[i:j+1]) for i in range(9) for j in range(i, 9)]
        return sorted(x for x in a if low <= x <= high)