class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > limit*3: return 0
        hi = n-max(0,n-2*limit)
        lo = max(0,n-limit)
        def calc(x):
            return min(limit,x)-max(0,x-limit)+1
        def calc2(mi,mx):
            return (mi+mx)*(mx-mi+1)//2
        # print(lo,hi)
        if hi <= limit:
            return calc2(calc(lo),calc(hi))
        elif lo >= limit:
            return calc2(calc(hi),calc(lo))
        else:
            return calc2(calc(lo),calc(limit))+calc2(calc(hi),calc(limit))-limit-1
