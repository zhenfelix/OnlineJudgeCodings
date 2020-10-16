class Solution:
    def checkPalindromeFormation(self, A: str, B: str) -> bool:
        def find_idx(s):
            n = len(s)
            i, j = (n//2, n//2) if n&1 else (n//2-1, n//2)
            while i >= 0 and s[i] == s[j]:
                i -= 1
                j += 1
            return i, j

        def helper(a, b):
            i, j = find_idx(a)
            ii, jj = i, j
            while ii >= 0 and b[ii] == a[jj]:
                ii -= 1
                jj += 1
            if ii < 0:
                return True
            ii, jj = i, j
            while ii >= 0 and a[ii] == b[jj]:
                ii -= 1
                jj += 1
            return ii < 0

    def checkPalindromeFormation(self, a, b):
        i, j = 0, len(a) - 1
        while i < j and a[i] == b[j]:
            i, j = i + 1, j - 1
        s1, s2 = a[i:j + 1], b[i:j + 1]

        i, j = 0, len(a) - 1
        while i < j and b[i] == a[j]:
            i, j = i + 1, j - 1
        s3, s4 = a[i:j + 1], b[i:j + 1]

        return any(s == s[::-1] for s in (s1,s2,s3,s4))