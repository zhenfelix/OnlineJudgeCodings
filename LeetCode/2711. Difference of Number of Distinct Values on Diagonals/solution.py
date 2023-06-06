class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        topleft = [[0]*m for _ in range(n)]
        visited = [set() for _ in range(n+m)]
        for i in range(n):
            for j in range(m):
                if i and j:
                    topleft[i][j] = topleft[i-1][j-1]
                    v = grid[i-1][j-1]
                    if v not in visited[i-j]:
                        visited[i-j].add(v)
                        topleft[i][j] += 1
        bottomright = [[0]*m for _ in range(n)]
        visited = [set() for _ in range(n+m)]
        for i in range(n)[::-1]:
            for j in range(m)[::-1]:
                if i+1 < n and j+1 < m:
                    bottomright[i][j] = bottomright[i+1][j+1]
                    v = grid[i+1][j+1]
                    if v not in visited[i-j]:
                        visited[i-j].add(v)
                        bottomright[i][j] += 1
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = abs(topleft[i][j]-bottomright[i][j])
        return ans 