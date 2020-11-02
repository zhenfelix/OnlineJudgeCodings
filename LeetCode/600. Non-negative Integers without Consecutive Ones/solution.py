from functools import lru_cache
class Solution:
    @lru_cache(None)
    def findIntegers(self, num: int) -> int:
        if num == 0:
            return 1
        if num == 1:
            return 2
        n = len(bin(num)) - 2
        return self.findIntegers((1<<(n-1))-1) + self.findIntegers(min(num-(1<<(n-1)),(1<<(n-2))-1))
