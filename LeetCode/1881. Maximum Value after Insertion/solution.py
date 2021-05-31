class Solution:
    def maxValue(self, n: str, x: int) -> str:
        m = len(n)
        x = chr(ord('0')+x)
        if n[0] == '-':
            i = 1
            while i < m and n[i] <= x:
                i += 1
            return n[:i] + x + n[i:]
        else:
            i = 0
            while i < m and n[i] >= x:
                i += 1
            return n[:i] + x + n[i:]