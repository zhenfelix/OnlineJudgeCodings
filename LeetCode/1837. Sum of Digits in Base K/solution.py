class Solution:
    def sumBase(self, n: int, k: int) -> int:
        sums = 0
        while n:
            sums += (n%k)
            n //= k
        return sums