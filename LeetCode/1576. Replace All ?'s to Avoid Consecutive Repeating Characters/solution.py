class Solution:
    def modifyString(self, s: str) -> str:
        res = list(s)
        n = len(s)
        for i, ch in enumerate(s):
            if ch == '?':
                for a in range(26):
                    a = chr(ord('a')+a)
                    if (i==0 or res[i-1] != a) and (i==n-1 or res[i+1] != a):
                        res[i] = a 
                        break
        return ''.join(res)
