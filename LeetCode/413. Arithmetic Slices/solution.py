# class Solution:
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         n = len(A)
#         if n < 3:
#             return 0
#         left, right = 0, 2
#         res = 0
#         while right <= n:
#             # if A[right]-A[right-1] == A[left+1]-A[left]:
#             #     right += 1
#             if right >= n or A[right]-A[right-1] != A[left+1]-A[left]:
#                 cnt = right - left
#                 res += (cnt-1)*(cnt-2)//2
#                 left = right - 1
#             right += 1
#         return res

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        dp = 0
        res = 0
        for i in range(2,n):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp += 1
                res += dp
            else:
                dp = 0
        return res