class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        sq = {k*k: k for k in range(1,n+1)}
        for i in range(1,n+1):
            for j in range(1,n+1):
                v = i*i + j*j  
                if v in sq:
                    res += 1
        return res