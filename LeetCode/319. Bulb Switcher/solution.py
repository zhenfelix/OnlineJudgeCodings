# class Solution:
#     def bulbSwitch(self, n: int) -> int:
#         def factor(x):
#             if x < 3:
#                 return [0,1,0][x]
#             sq = int(n**0.5)+1
#             for f in range(2,sq):
#                 if x%f:
#                     continue
#                 cnt = 0
#                 while x%f == 0:
#                     x //= f 
#                     cnt ^= 1
#                 if cnt == 1:
#                     return 0
#             return 1 if x == 1 else 0
#         return sum(factor(i) for i in range(1,n+1))
#                 

# class Solution:
#     def bulbSwitch(self, n: int) -> int:
#         arr = [0]*(n+1)
#         for i in range(1,n+1):
#             j = 1
#             while i*j <= n:
#                 arr[i*j] ^= 1
#                 j += 1
#         return sum(arr)
                

import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        # return int(n**0.5)
        return int(math.sqrt(n))
                