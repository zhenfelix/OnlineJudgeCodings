import math

# class Solution:
#     def maximumSum(self, arr: List[int]) -> int:
#         n = len(arr)
#         left, right = arr.copy(), arr.copy()
#         for i in range(1,n):
#             left[i] = max(left[i], left[i]+left[i-1])
#         for i in range(n-2,-1,-1):
#             right[i] = max(right[i], right[i]+right[i+1])
#         res = -math.inf
#         i = -1
#         while i <= n:
#             l, r = -math.inf, -math.inf
#             if i > 0:
#                 l = left[i-1]
#             if i < n-1:
#                 r = right[i+1]
#             res = max(res,l,r,l+r)
#             i += 1
#         return res

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp0, dp1, res = arr[0], 0, arr[0]
        for i in range(1,n):
            dp0, dp1 = max(dp0+arr[i], arr[i]), max(dp0,dp1+arr[i])
            res = max(dp0, dp1, res)
        return res
                
        