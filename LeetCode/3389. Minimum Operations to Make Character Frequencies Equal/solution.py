class Solution:
    def makeStringGood(self, s: str) -> int:
        n = len(s)
        cc = [0]*26
        for ch in s:
            cc[ord(ch)-ord('a')] += 1

        @lru_cache(None)
        def dfs(i,flag,y):
            if i == 0:
                return cc[i] if flag == 0 else abs(cc[i]-y)
            if flag == 0:
                return min(dfs(i-1,0,y),dfs(i-1,1,y))+cc[i]
            if cc[i] >= y:
                return min(dfs(i-1,0,y),dfs(i-1,1,y))+cc[i]-y
            d = y-cc[i]
            return min(dfs(i-1,0,y)+d-min(d,cc[i-1]),dfs(i-1,1,y)+d-min(d,max(0,cc[i-1]-y)))

        ans = min(min(dfs(25,0,y),dfs(25,1,y)) for y in range(n+1))
        dfs.cache_clear()
        return ans 