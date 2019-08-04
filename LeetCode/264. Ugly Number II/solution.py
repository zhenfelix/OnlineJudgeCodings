# import math

# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         dp = [1,2,3,4,5]
#         if n < 6:
#             return dp[n-1]
#         for i in range(5,n):
#             left, right = 0, i-1
#             num = math.inf
#             while left <= right:
#                 if dp[left]*dp[right] <= dp[-1]:
#                     left += 1
#                 elif dp[left]*dp[right] < num:
#                     num = dp[left]*dp[right]
#                     right -= 1
#                 else:
#                     right -= 1
#             dp.append(num)
#         return dp[-1]


import math

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
       
        i, j, k = 0, 0, 0
        for idx in range(1,n):
            while dp[i]*2 <= dp[-1]:
                i += 1
            while dp[j]*3 <= dp[-1]:
                j += 1
            while dp[k]*5 <= dp[-1]:
                k += 1
            
            dp.append(min(dp[i]*2,dp[j]*3,dp[k]*5))
        # print(dp)
        return dp[-1]