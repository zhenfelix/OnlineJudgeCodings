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



from functools import lru_cache
class Solution:
    def findIntegers(self, n: int) -> int:
        @lru_cache(None)
        def dfs(x, flag):
            if x == 1:
                return flag
            if x == 0:
                return flag^1
            if flag == 1:
                return dfs((x>>1)-(x&1), 0)
            return dfs(x>>1,0) + dfs(x>>1,1)
        return dfs(n,0)+dfs(n,1)

