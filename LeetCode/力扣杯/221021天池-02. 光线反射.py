class Solution:
    def getLength(self, grid: List[str]) -> int:
        dxy = [(1,0),(0,1),(-1,0),(0,-1)]
        cur = (0,0,0)
        cnt = 0
        n, m = len(grid), len(grid[0])
        L = [1,0,3,2]
        R = [3,2,1,0]
        while True:
            x, y, k = cur
            if x < 0 or x >= n or y < 0 or y >= m:
                return cnt
            ch = grid[x][y]
            if ch == 'L':
                k = L[k]
            elif ch == 'R':
                k = R[k]
            dx, dy = dxy[k]
            cur = (x+dx,y+dy,k)
            cnt += 1
        return -1