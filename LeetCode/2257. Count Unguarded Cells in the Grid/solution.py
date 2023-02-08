class Solution:
    def countUnguarded(self, n: int, m: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['.']*m for _ in range(n)]
        for r, c in guards:
            grid[r][c] = 'G'
        for r, c in walls:
            grid[r][c] = 'W'

        def operate(r,c,flag):
            if grid[r][c] == 'W':
                flag = False
            elif grid[r][c] == 'G':
                flag = True
            elif flag:
                grid[r][c] = '#'
            return flag

        for r in range(n):
            flag = False
            for c in range(m):
                flag = operate(r,c,flag)
            flag = False
            for c in range(m)[::-1]:
                flag = operate(r,c,flag)
        for c in range(m):
            flag = False
            for r in range(n):
                flag = operate(r,c,flag)
            flag = False
            for r in range(n)[::-1]:
                flag = operate(r,c,flag)
        return sum(ch == '.' for row in grid for ch in row)

                
                
                
                
                
                



class Solution:
    def countUnguarded(self, n: int, m: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards = set([(r,c) for r, c in guards])
        walls = set([(r,c) for r, c in walls])
        visited = set()
        visible = False
        # print(guards,walls)

        def doit(i,j):
            nonlocal visible
            if (i,j) in guards or (i,j) in walls:
                # print(i,j,"gw")
                visited.add((i,j))
            if (i,j) in guards:
                visible = True
            if (i,j) in walls:
                visible = False
            if visible:
                # print(i,j,"visible")
                visited.add((i,j))

        for i in range(n):
            visible = False
            for j in range(m):
                doit(i,j)
            visible = False
            for j in range(m)[::-1]:
                doit(i,j)            
            
            
        for j in range(m):
            visible = False
            for i in range(n):
                doit(i,j)
            visible = False
            for i in range(n)[::-1]:
                doit(i,j)

        return m*n-len(visited)