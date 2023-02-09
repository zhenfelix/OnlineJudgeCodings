class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        m = len(t)
        for i, ch in enumerate(s):
            if j >= m:
                break  
            if t[j] == ch:
                j += 1
        return m-j