class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = []
        while n:
            # print(n,k)
            if k <= 1 + 26*(n-1):
                res.append('a')
                k -= 1
            else:
                r = k - 26*(n-1)
                ch = chr(ord('a')+r-1)
                res.append(ch)
                k -= r 
            n -= 1
        return ''.join(res)
