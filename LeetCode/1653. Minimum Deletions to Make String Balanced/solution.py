class Solution:
    def minimumDeletions(self, s: str) -> int:
        a = s.count('a')
        b = 0
        res = len(s)
        for ch in s:
            if ch == 'b':
                res = min(res, a + b)
                b += 1
            else:
                a -= 1
        return min(res, a+b)


class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a, b = [0]*n, [0]*n
        cnt = 0
        for i in range(n):
            if s[i] == 'b':
                cnt += 1
            b[i] = cnt
        cnt = 0
        for i in range(n)[::-1]:
            if s[i] == 'a':
                cnt += 1
            a[i] = cnt
        res = n
        a.append(0)
        b.append(0)
        for i in range(n+1):
            res= min(res,b[i-1]+a[i])
        return res