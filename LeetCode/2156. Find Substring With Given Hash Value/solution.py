class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        h = 0
        q = 1
        n = len(s)
        res = -1
        def val(ch):
            return ord(ch)-ord('a')+1

        for i in range(n-k,n):
            h += val(s[i])*q
            h %= modulo
            if i < n-1:
                q *= power
                q %= modulo
        if h == hashValue:
            res = n-k
        # print(n-k,h)
        for i in range(n-k)[::-1]:
            h -= (val(s[i+k])*q)%modulo
            h = (h+modulo)%modulo
            h *= power
            h += val(s[i])
            h %= modulo
            # print(i,h)
            if h == hashValue:
                res = i 
        # print(res)
        return s[res:res+k]