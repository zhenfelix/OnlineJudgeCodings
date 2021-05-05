class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(ch, x):
            return chr(ord(ch)+x)
        res = []
        n = len(s)
        for i in range(0,n,2):
            res.append(s[i])
            if i+1 < n:
                res.append(shift(s[i], int(s[i+1])))
        return "".join(res)