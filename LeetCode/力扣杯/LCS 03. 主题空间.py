class Solution:
    def largestArea(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])
        grid = [list(s)+['0'] for s in grid]
        grid += [['0']*(m+1)]
        res, VISITED = 0, '#'
        dxy = [-1,0,1,0,-1]
        def dfs(ch,x,y):
            grid[x][y] = '#'
            flag, cnt = True, 1
            for dx, dy in zip(dxy,dxy[1:]):
                dx += x
                dy += y
                if grid[dx][dy] == ch:
                    f, c = dfs(ch,dx,dy)
                    cnt += c 
                    flag &= f 
                if grid[dx][dy] == '0':
                    flag &= False
            return flag, cnt 



        for i in range(n):
            for j in range(m):
                if ord(grid[i][j]) > ord('0'):
                    flag, cnt = dfs(grid[i][j], i, j)
                    if flag:
                        res = max(res, cnt) 
        return res
