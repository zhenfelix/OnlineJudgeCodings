import functools
class Solution:
    def ways(self, pizza: List[str], K: int) -> int:
        n, m = len(pizza), len(pizza[0])
        Mod = 10**9+7
        cnt = [[0]*m for _ in range(n)]
        for i in range(n)[::-1]:
            for j in range(m)[::-1]:
                dl = cnt[i+1][j] if i+1 < n else 0
                ur = cnt[i][j+1] if j+1 < m else 0
                dr = cnt[i+1][j+1] if (i+1 < n and j+1 < m) else 0
                cnt[i][j] = (pizza[i][j] == 'A') + dl + ur - dr 
        # print(cnt)
        @functools.lru_cache(None)
        def dfs(r,c,k):
            if k == 1:
                return (cnt[r][c] >= 1) * 1
            if cnt[r][c] < k:
                return 0
            res = 0
            for x in range(r+1,n):
                res += (cnt[r][c]-cnt[x][c] > 0) * dfs(x,c,k-1)
            for y in range(c+1,m):
                res += (cnt[r][c]-cnt[r][y] > 0) * dfs(r,y,k-1)
            return res%Mod
        return dfs(0,0,K)
