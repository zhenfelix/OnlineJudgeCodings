class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        g = divisor1*divisor2//gcd(divisor1,divisor2)
        def check(t):
            c = t//g 
            c1, c2 = t//divisor2-c, t//divisor1-c
            return max(0,uniqueCnt1-c1)+max(0,uniqueCnt2-c2) <= t-c-c1-c2

        lo, hi = 1, 2*10**9
        while lo <= hi:
            m = (lo+hi)//2
            if check(m):
                hi = m-1
            else:
                lo = m+1
        return lo 