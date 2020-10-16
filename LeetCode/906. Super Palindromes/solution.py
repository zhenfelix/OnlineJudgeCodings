class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        def isPalind(s):
            return s == s[::-1]
        def palind_genrator():
            for i in range(10):
                yield i 
            for i in range(1,10**4):
                tmp = str(i)
                yield int(tmp+tmp[::-1])
                for j in range(10):
                    yield int(tmp+str(j)+tmp[::-1])

        left, right = int(L), int(R)
        cnt = 0
        for x in palind_genrator():
            y = x**2
            if left <= y <= right and isPalind(str(y)):
                cnt += 1
        return cnt