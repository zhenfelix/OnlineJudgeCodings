class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        @lru_cache(None)
        def dfs(ch,a,b,c):
            ans = 0
            if ch == 0:
                if b > 0:
                    ans = max(ans,dfs(1,a,b-1,c)+1)
            else:
                if a > 0:
                    ans = max(ans,dfs(0,a-1,b,c)+1)
                if c > 0:
                    ans = max(ans,dfs(2,a,b,c-1)+1)
            return ans
        return max(dfs(i,x,y,z) for i in range(3))*2

class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x == y: return (x+y+z)*2
        if x < y: return (x*2+1+z)*2
        return (y*2+1+z)*2

