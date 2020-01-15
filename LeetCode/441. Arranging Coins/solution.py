class Solution:
    def arrangeCoins(self, n: int) -> int:
        n *= 2
        x = int(math.sqrt(n))
        while x*(x+1) > n:
            x -= 1
        return x