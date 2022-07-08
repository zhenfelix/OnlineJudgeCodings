class Solution:
    def greatestLetter(self, s: str) -> str:
        up, low = set(), set()
        for ch in s:
            if ch.islower():
                low.add(ch)
            else:
                up.add(ch)
        for i in range(26)[::-1]:
            l = chr(ord('a')+i)
            u = chr(ord('A')+i)
            if l in low and u in up:
                return u  
        return ""