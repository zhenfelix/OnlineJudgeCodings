class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append((grid[i][j],i,j))
        arr.sort(reverse=True)
        print(arr)
        tot = n*m  
        mask = (1<<n)-1
        @lru_cache(None)
        def dfs(idx,s):
            if idx >= n*m: return 0
            if s == mask: return 0
            v,r,c = arr[idx]
            ans = dfs(idx+1,s)
            if( (s>>r)&1) == 0:
                while idx+1 < tot and arr[idx+1][0] == v: idx += 1
                ans = max(ans,dfs(idx+1,s|(1<<r))+v)
            # print(idx,s,ans)
            return ans 
        return dfs(0,0)