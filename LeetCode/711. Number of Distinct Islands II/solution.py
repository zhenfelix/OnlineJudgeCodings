class Solution(object):
    def numDistinctIslands2(self, grid):
        seen = set()
        def explore(r, c):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.add(complex(r, c))
                explore(r+1, c)
                explore(r-1, c)
                explore(r, c+1)
                explore(r, c-1)

        def canonical(shape):
            def translate(shape):
                w = complex(min(z.real for z in shape),
                            min(z.imag for z in shape))
                return sorted(str(z-w) for z in shape)

            ans = []
            for k in range(4):
                ans = max(ans, translate([z * (1j)**k for z in shape]))
                ans = max(ans,  translate([complex(z.imag, z.real) * (1j)**k
                                           for z in shape]))
            return tuple(ans)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c)
                if shape:
                    shapes.add(canonical(shape))

        return len(shapes)





class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        shapes = set()
        drc = [-1,0,1,0,-1]

        def valid(r,c):
            return 0 <= r < n and 0 <= c < m and grid[r][c] == 1 and (r,c) not in visited

        def bfs(r,c):
            shape = []
            lor, hir = float('inf'), -float('inf')
            loc, hic = float('inf'), -float('inf')
            if not valid(i,j):
                return shape, (lor,hir), (loc,hic)
            visited.add((r,c))
            q = deque()
            q.append((r,c))
            while q:
                r, c = q.popleft()
                shape.append((r,c))
                lor = min(lor, r)
                hir = max(hir, r)
                loc = min(loc, c)
                hic = max(hic, c)
                for dr, dc in zip(drc[1:],drc[:-1]):
                    dr += r 
                    dc += c 
                    if valid(dr,dc):
                        visited.add((dr,dc))
                        q.append((dr,dc))
            return shape, (lor,hir), (loc,hic)

        def hash(shape, lhr, lhc):
            lor,hir = lhr
            loc,hic = lhc
            ans = [[] for _ in range(8)]
            for i, baser in enumerate(lhr):
                for j, basec in enumerate(lhc):
                    idx = i*2+j
                    for r, c in shape:
                        x, y = abs(r-baser), abs(c-basec)
                        ans[idx*2].append((x,y))
                        ans[idx*2+1].append((y,x))
            return tuple(max([sorted(s) for s in ans]))

        for i in range(n):
            for j in range(m):
                shape, lhr, lhc = bfs(i,j)
                if shape:
                    # print(shape, lhr, lhc)
                    shapes.add(hash(shape, lhr, lhc))
                    # shapes.add(len(shape))
                    # weak test cases, most shapes with the same size are identical
        # print(shapes)
        return len(shapes)





