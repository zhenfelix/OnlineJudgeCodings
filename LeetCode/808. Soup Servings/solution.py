class Solution:
    def soupServings(self, n: int) -> float:
        n = (n-1)//25+1
        if n > 1000:
            return 1
        @lru_cache(None)
        def dfs(x, y):
            if x <= 0 and y <= 0:
                return 0.5
            if x <= 0:
                return 1
            if y <= 0:
                return 0 
            return 0.25*(dfs(x-4,y)+dfs(x-3,y-1)+dfs(x-2,y-2)+dfs(x-1,y-3))
        return dfs(n,n)
