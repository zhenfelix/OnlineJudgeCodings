class Solution:
    def secondHighest(self, s: str) -> int:
        s = set(ch for ch in s if '0' <= ch <= '9')
        s = sorted(list(s))
        if len(s) < 2:
            return -1
        return int(s[-2])