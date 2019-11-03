class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x, y = 0, 0
        for ch1, ch2 in zip(s1,s2):
            if ch1 != ch2:
                if ch1 == 'x':
                    x += 1
                else:
                    y += 1
        if x%2 != y%2:
            return -1
        return x//2+y//2+x%2+y%2