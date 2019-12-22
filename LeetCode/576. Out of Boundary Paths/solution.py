# from functools import lru_cache
# class Solution:
#     def findPaths(self, n: int, m: int, N: int, i: int, j: int) -> int:
#         @lru_cache(None)
#         def dfs(r,c,s):
#             if r < 0 or r >= n or c < 0 or c >= m:
#                 return 1
#             if s <= 0:
#                 return 0
#             return sum(dfs(rr,cc,s-1) for rr, cc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)])
#         return dfs(i,j,N)%(10**9+7)


from functools import lru_cache
class Solution:
    @lru_cache(None)
    def findPaths(self, n: int, m: int, s: int, r: int, c: int) -> int:
        if r < 0 or r >= n or c < 0 or c >= m:
            return 1
        if s <= 0:
            return 0
        return sum(self.findPaths(n,m,s-1,rr,cc) for rr, cc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)])%(10**9+7)
            
            
    