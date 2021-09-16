class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        def gcd(a,b):
            if b == 0:
                return a 
            return gcd(b, a%b)

        cc = Counter()
        res = 0
        for w, h in rectangles:
            g = gcd(w,h)
            w, h = w//g, h//g 
            res += cc[w,h]
            cc[w,h] += 1
        return res