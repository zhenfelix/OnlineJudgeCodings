class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)
        mx, mi = -1, n
        for i, ch in enumerate(s):
            if ch == 'a':
                mx = max(mx, i)
            else:
                mi = min(mi, i)
        return mx < mi