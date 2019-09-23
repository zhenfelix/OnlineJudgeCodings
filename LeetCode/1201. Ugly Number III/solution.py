# class Solution:
#     def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
#         def gcd(x, y):
#             while(y):
#                 x, y = y, x % y
#             return x 
#         def lcm(x, y):
#             return x*y//gcd(x,y)
#         # d = gcd(a, gcd(b,c))
#         abc = lcm(a,lcm(b,c))
#         base = (abc//a) + (abc//b) + (abc//c) - (abc//lcm(a,b)) - (abc//lcm(a,c)) - (abc//lcm(c,b)) + 1
#         # print(abc)
#         # print(base)
        
#         t = (n//base)
#         cnt = base*t
#         xa, xb, xc = a+abc*t, b+abc*t, c+abc*t
#         res = abc*t
#         while cnt < n:
#             res = min(xa, xb, xc)
#             if res == xa:
#                 xa += a
#             if res == xb:
#                 xb += b
#             if res == xc:
#                 xc += c
#             cnt += 1
#         return res

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(x, y):
            while(y):
                x, y = y, x % y
            return x 
        def lcm(x, y):
            return x*y//gcd(x,y)
       
        def rankUglyNumber(x, a, b, c):
            rank = x//a + x//b + x//c
            rank -= (x//lcm(a,b) + x//lcm(b,c) + x//lcm(a,c))
            rank += x//lcm(a,lcm(b,c))
            return rank
        
        lo, hi = 0, 2*10**9
        while lo <= hi:
            mid = (lo + hi)//2
            if rankUglyNumber(mid, a, b, c) >= n:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return lo