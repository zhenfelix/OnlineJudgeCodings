# class Solution(object):
#     def checkRecord(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         P0, L0, LL0, A1, P1, L1, LL1 = 1, 1, 0, 1, 0, 0, 0
#         MOD = (10**9)+7
#         for i in range(2, n+1):
#             P0, L0, LL0, A1, P1, L1, LL1 = (P0+L0+LL0)%MOD, P0%MOD, L0%MOD, (P0+L0+LL0)%MOD, (A1+P1+L1+LL1)%MOD, (A1+P1)%MOD, L1%MOD
#             # print(P0, L0, LL0, A1, P1, L1, LL1)
#         return (P0 + L0 + LL0 + A1 + P1 + L1 + LL1)%MOD
        

import numpy as np

class Solution(object):
    def checkRecord(self, n):
        A = np.matrix([[0, 0, 1, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0],
                       [0, 1, 1, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1],
                       [0, 0, 1, 1, 0, 1],
                       [0, 0, 1, 0, 1, 1]])
        power = A
        mod = 10**9 + 7
        while n:
            if n & 1:
                power = (power * A) % mod
            A = A**2 % mod
            n //= 2
        return int(power[5, 2])