# class Solution:
#     def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
#         def gcd(x,y):
#             x, y = max(x,y), min(x,y)
#             while y != 0:
#                 x, y = y, x%y
#             return x
#         mod = 10**9 + 7
#         L = A*B//gcd(A,B)
#         M = L//A + L//B - 1
#         t, r = N//M, N%M
#         if r == 0:
#             return L*t%mod
#         a, b = A, B
#         for _ in range(r-1):
#             if a < b:
#                 a += A
#             else:
#                 b += B
#         return (L*t+min(a,b))%mod


class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        def gcd(x,y):
            x, y = max(x,y), min(x,y)
            while y != 0:
                x, y = y, x%y
            return x
        mod = 10**9 + 7
        L = A*B//gcd(A,B)
        lo, hi = 2, 10**14
        while lo <= hi:
            mid = (lo+hi)//2
            if mid//A+mid//B-mid//L < N:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo%(10**9+7)
        
