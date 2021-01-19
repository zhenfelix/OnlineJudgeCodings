class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        n, m = len(grid), len(grid[0])
        def bfs(x,y):
            visited = set()
            visited.add((x,y))
            q = deque()
            q.append((x,y))
            while q:
                r, c = q.popleft()
                for dr, dc in [(0,-1),(0,1),(-1,0),(1,0)]:
                    dr += r
                    dc += c 
                    if 0 <= dr < n and 0 <= dc < m and (dr,dc) not in visited and grid[dr][dc] != '#':
                        visited.add((dr,dc))
                        q.append((dr,dc))
            return visited

        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                if ch == 'C':
                    catReach = bfs(i,j)
                    cat = (i,j)
                if ch == 'M':
                    mouseReach = bfs(i,j)
                    mouse = (i,j)
                if ch == 'F':
                    food = (i,j)
        # print(catReach,mouseReach,cat,mouse,food)
        
        def available(x,y,delta):
            yield x, y
            for dx, dy in [(0,-1),(0,1),(-1,0),(1,0)]:
                for k in range(1,delta+1):
                    xx, yy = x+dx*k, y+dy*k
                    if xx >= n or xx < 0 or yy >= m or yy < 0 or grid[xx][yy] == '#':
                        break
                    yield xx, yy
            return 0
        degree = Counter()
        for cat_x, cat_y in catReach:
            for mouse_x, mouse_y in mouseReach:
                for _, _ in available(cat_x,cat_y,catJump):
                    degree[cat_x,cat_y,mouse_x,mouse_y,True] += 1
                for _, _ in available(mouse_x,mouse_y,mouseJump):
                    degree[cat_x,cat_y,mouse_x,mouse_y,False] += 1
        pq = deque()
        seen = {}
        for x, y in catReach&mouseReach:
            seen[x,y,x,y,False] = False
            pq.append((x,y,x,y,False))
        for x, y in catReach:
            seen[x,y,food[0],food[1],True] = False
            pq.append((x,y,food[0],food[1],True))
        for x, y in mouseReach:
            seen[food[0],food[1],x,y,False] = False
            pq.append((food[0],food[1],x,y,False))

        # for x, y in catReach&mouseReach:
        #     if (x,y) == food:
        #         continue
        #     seen[x,y,x,y,False] = False
        #     seen[x,y,x,y,True] = True
        #     pq.append((x,y,x,y,False))
        #     pq.append((x,y,x,y,True))
        # for x, y in catReach:
        #     if (x,y) == food:
        #         continue
        #     seen[x,y,food[0],food[1],True] = False
        #     pq.append((x,y,food[0],food[1],True))
        # for x, y in mouseReach:
        #     if (x,y) == food:
        #         continue
        #     seen[food[0],food[1],x,y,False] = False
        #     pq.append((food[0],food[1],x,y,False))
        # print(seen)
        while pq:
            cat_x, cat_y, mouse_x, mouse_y, cat_turn = pq.popleft()
            win = seen[cat_x, cat_y, mouse_x, mouse_y, cat_turn]
            if (cat_x,cat_y) == cat and (mouse_x,mouse_y) == mouse and not cat_turn:
                return win 
            if cat_turn:
                for x, y in available(mouse_x,mouse_y,mouseJump):
                    degree[cat_x,cat_y,x,y,not cat_turn] -= 1
                    if (cat_x,cat_y,x,y,not cat_turn) in seen:
                        continue
                    if win and degree[cat_x,cat_y,x,y,not cat_turn] > 0:
                        continue
                    seen[cat_x,cat_y,x,y,not cat_turn] = not win
                    pq.append((cat_x,cat_y,x,y,not cat_turn))
            else:
                for x, y in available(cat_x,cat_y,catJump):
                    degree[x,y,mouse_x,mouse_y, not cat_turn] -= 1
                    if (x,y,mouse_x,mouse_y,not cat_turn) in seen:
                        continue
                    if win and degree[x,y,mouse_x,mouse_y,not cat_turn] > 0:
                        continue
                    seen[x,y,mouse_x,mouse_y,not cat_turn] = not win
                    pq.append((x,y,mouse_x,mouse_y,not cat_turn))
        return False


