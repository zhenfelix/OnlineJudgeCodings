class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def calc(x):
            return sum(map(int,list(str(x))))
        cur = calc(n)
        if cur <= target:
            return 0
        s = str(n)
        ans, base = 0, 1
        for ch in s[::-1]:
            ch = int(ch)
            cur -= ch
            ans += (9-ch)*base
            if cur+1 <= target:
                return ans+1
            base *= 10

        return -1

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def calc(x):
            return sum(map(int,list(str(x))))
        base = 1
        while True:
            nxt = n//base*base+base if base > 1 else n 
            if calc(nxt) <= target:
                return nxt-n
            base *= 10
        return -1