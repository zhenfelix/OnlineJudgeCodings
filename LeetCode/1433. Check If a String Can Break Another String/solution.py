class Solution:
    def check(self, d1, d2):
        s = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            s += d1[c] - d2[c]
            if s < 0:
                return False
        return True
    
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        d1 = collections.Counter(s1)
        d2 = collections.Counter(s2)
        return self.check(d1, d2) | self.check(d2, d1)


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def cmp(A,B):
            for a, b in zip(A,B):
                if a < b:
                    return False
            return True

        s1 = ''.join(sorted(list(s1))[::-1])
        s2 = ''.join(sorted(list(s2))[::-1])
        return cmp(s1,s2) or cmp(s2,s1)