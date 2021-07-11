class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        drc = [-1,0,1,0,-1]
        r, c = entrance
        q = [(r,c)]
        maze[r][c] = '+'
        step = 0
        n, m = len(maze), len(maze[0])
        while q:
            nq = []
            for r, c in q:
                if (r in [0,n-1] or c in [0,m-1]) and ([r,c] != entrance):
                    return step
                for dr, dc in zip(drc, drc[1:]):
                    dr += r 
                    dc += c  
                    if not (0 <= dr < n) or not (0 <= dc < m):
                        continue
                    if maze[dr][dc] == '.':
                        nq.append((dr,dc))
                        maze[dr][dc] = '+'
            step += 1 
            q = nq 
        return -1