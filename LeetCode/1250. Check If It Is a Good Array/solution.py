from math import gcd
from functools import reduce
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1


# class Solution:
#     def isGoodArray(self, nums: List[int]) -> bool:
#         def gcd(a,b):
#             a, b = max(a,b), min(a,b)
#             while b != 0:
#                 a, b = b, a%b
#             return a
#         n = len(nums)
#         pre = nums[0]
#         if pre == 1:
#             return True
#         for i in range(1,n):
#             cur = nums[i]
#             res = gcd(pre,cur)
#             if res == 1:
#                 return True
#             pre = res
#         return False

    # def isGoodArray(self, A):
    #     gcd = A[0]
    #     for a in A:
    #         while a:
    #             gcd, a = a, gcd % a
    #     return gcd == 1