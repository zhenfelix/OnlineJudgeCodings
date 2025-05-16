class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,r,t):
            if i == n-1:
                return inf if r > 0 else 0
            j = i+1
            cur = time[j]
            ans = t*(position[j]-position[i])+dfs(j,r,cur)
            while r > 0 and j+1 < n:
                r -= 1
                j += 1
                cur += time[j]
                ans = min(ans, t*(position[j]-position[i])+dfs(j,r,cur))
            return ans 
        return dfs(0,k,time[0])