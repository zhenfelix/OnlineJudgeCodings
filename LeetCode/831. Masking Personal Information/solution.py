class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            a, b = s.split('@')
            a, b = a.lower(), b.lower()
            return a[0]+'*'*5+a[-1]+'@'+b
        else:
            s = ''.join([ch for ch in s if '0' <= ch <= '9'])
            res = "***-***-"+s[-4:]
            if len(s) > 10:
                res = "+"+'*'*(len(s)-10)+"-"+res
            return res
        