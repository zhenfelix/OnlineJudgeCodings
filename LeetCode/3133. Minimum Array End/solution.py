class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        for i in range(64):
            if (x>>i)&1: continue
            if n&1: x |= (1<<i)
            n >>= 1
        return x 