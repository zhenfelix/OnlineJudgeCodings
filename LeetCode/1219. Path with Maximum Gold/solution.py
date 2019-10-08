class Solution:
  def getMaximumGold(self, grid: List[List[int]]) -> int:
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    def dfs(i, j, visited):
      res = 0
      if 0 <= i < n and 0 <= j < m and (i,j) not in visited and grid[i][j] > 0:
        res += grid[i][j]
        visited.add((i,j))
        tmp = 0
        for k in range(4):
          tmp = max(tmp, dfs(i+dx[k], j+dy[k], visited))
        res += tmp
        visited.remove((i,j))
      return res

    ans = 0
    n, m = len(grid), len(grid[0])
    for x in range(n):
      for y in range(m):
        ans = max(ans, dfs(x,y,set()))
    return ans

    