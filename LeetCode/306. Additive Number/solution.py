class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i, j in itertools.combinations(range(1,n),2):
            a, b = num[:i], num[i:j]
            if b != str(int(b)) or a != str(int(a)):
                continue
            while j < n:
                c = str(int(a)+int(b))
                
                if not num[j:].startswith(c):
                    break
                j += len(c)
                a, b = b, c
            if j == n:
                return True
        return False