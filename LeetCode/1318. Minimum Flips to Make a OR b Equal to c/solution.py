class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        for i in range(32):
            x, y, z = a&(1<<i), b&(1<<i), c&(1<<i)
            if x|y != z:
                if z == 0:
                    cnt += (x!=0) + (y!=0)
                else:
                    cnt += 1
        return cnt