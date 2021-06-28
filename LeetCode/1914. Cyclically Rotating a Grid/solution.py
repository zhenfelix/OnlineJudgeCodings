class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        def get_round(x,y):
            return min(x,y,n-1-x,m-1-y)
        def get_pos(x,y,r):
            if x == r or y == m-1-r:
                return x-r+y-r
            else:
                return n-1-r-x+m-1-r-y+n-1-r*2+m-1-r*2

        res = [[0]*m for _ in range(n)]
        mp = {}
        for i in range(n):
            for j in range(m):
                r = get_round(i,j)
                pos = get_pos(i,j,r)
                # print(i,j,r,pos)
                mp[r,pos] = (i,j)

        # print(mp)
        for i in range(n):
            for j in range(m):
                r = get_round(i,j)
                sz = (n-r*2)*2+(m-r*2)*2-4
                # print(sz)
                pos = get_pos(i,j,r)
                x, y = mp[r,(pos+k)%sz]
                res[i][j] = grid[x][y]
        return res 
