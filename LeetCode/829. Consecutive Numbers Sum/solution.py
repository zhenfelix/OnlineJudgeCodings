# class Solution(object):
#     def consecutiveNumbersSum(self, N):
#         """
#         :type N: int
#         :rtype: int
#         """
#         res = 1
#         left, right = N//2, N//2 + 1
#         while right > 0:
#             while left > 0 and (left+right)*(right-left+1)//2 < N:
#                 left -= 1
#             if left == 0:
#                 break
#             if (left+right)*(right-left+1)//2 == N:
#                 # print(left,right)
#                 res += 1
#             right -= 1
#         return res

#         
import math
class Solution(object):
    # def consecutiveNumbersSum(self, N):
    #     """
    #     :type N: int
    #     :rtype: int
    #     """
    #     res = 0
    #     for m in range(1,int(math.sqrt(2*N))+1):
    #         if (2*N)%m == 0 and ((2*N//m)+1-m)%2 == 0:
    #             res += 1
    #     return res
    
    def consecutiveNumbersSum(self, N):
        res = 1
        i = 3
        while N % 2 == 0:
            N //= 2
        while i * i <= N:
            count = 0
            while N % i == 0:
                N //= i
                count += 1
            res *= count + 1
            i += 2
        return res if N == 1 else res * 2

        