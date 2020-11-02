class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         i = 0
#         while i*i <= num:
#             if i*i == num:
#                 return True
#             i += 1
#         return False
        
    def isPerfectSquare(self, num):
        left = 0
        right = num
        
        while left <= right:
            mid = left + (right-left)//2
            if  mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid -1
            else:
                left = mid +1
        return False