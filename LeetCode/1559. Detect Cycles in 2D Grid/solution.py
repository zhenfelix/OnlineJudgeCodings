import sys
sys.setrecursionlimit(10**6)

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        seen = [[False]*m for _ in range(n)]

        def dfs(i,j,parent):
            
            seen[i][j] = True
            for ni, nj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni += i 
                nj += j
                if ni < 0 or ni >= n or nj < 0 or nj>= m or (ni,nj) == parent or grid[ni][nj] != grid[i][j]:
                    continue
                if seen[ni][nj] or dfs(ni,nj,(i,j)):
                    return True
            return False


        for r in range(n):
            for c in range(m):
                if not seen[r][c]:
                    if dfs(r,c,(-1,-1)):
                        return True
                    # print(r,c,seen,depth)
        return False