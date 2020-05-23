class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a,b):
            if a < b:
                a, b = b, a
            while b:
                a, b = b, a%b
            return a
        res = []
        for y in range(2,n+1):
            for x in range(1,y):
                if gcd(x,y) == 1:
                    res.append("{}/{}".format(str(x),str(y)))
        return res