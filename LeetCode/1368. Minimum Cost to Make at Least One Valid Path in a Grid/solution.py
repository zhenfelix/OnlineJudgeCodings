class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        n, m = len(grid), len(grid[0])
        dr, dc = [0,0,1,-1], [1,-1,0,0]
        def reach(r,c):
            while (0 <= r < n) and (0 <= c < m) and (r,c) not in visited:
                # print(r,c)
                visited.add((r,c))
                q.append((r,c))
                idx = grid[r][c]-1
                r, c = r+dr[idx], c+dc[idx]
        reach(0,0)
        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                x, y = q.popleft()
                # print('x',x,'y',y)
                if (x,y) == (n-1,m-1):
                    return step
                for i in range(4):
                    reach(x+dr[i],y+dc[i])
            step += 1
        return -1


            
