# class Solution:
#     def maxNiceDivisors(self, n):
#         M = 10**9 + 7
#         if n <= 3: return n
#         if n % 3 == 0: return pow(3, n//3, M)
#         if n % 3 == 1: return (pow(3, (n-4)//3, M) * 4) % M
#         return (2*pow(3, n//3, M)) % M

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors == 1:
            return 1
        if primeFactors%3 == 0:
            p, q = 0, primeFactors//3
        elif primeFactors%3 == 1:
            p, q = 2, primeFactors//3-1
        else:
            p, q = 1, primeFactors//3
        MOD = 10**9+7
        def quickMul(a, x):
            if x == 0:
                return 1
            res = quickMul(a, x//2)**2
            if x%2 == 1:
                res *= a
            res %= MOD
            return res

        return 2**p*quickMul(3,q)%MOD