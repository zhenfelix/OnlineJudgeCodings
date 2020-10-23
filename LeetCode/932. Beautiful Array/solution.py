from functools import lru_cache
class Solution(object):
    @lru_cache(None)
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        if N == 1:
            return [1]
        left = self.beautifulArray(N//2)
        right = self.beautifulArray(N//2+(N&1))
        return [x*2 for x in left] + [x*2-1 for x in right]


    def beautifulArray(self, N):
        res = [1]
        while len(res) < N:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
        return [i for i in res if i <= N]