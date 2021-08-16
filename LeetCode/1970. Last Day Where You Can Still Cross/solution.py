class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0]*col for _ in range(row)]
        n = len(cells)
        for r, c in cells:
            r -= 1
            c -= 1
            grid[r][c] = 1
        # print(grid)
        tot = row*col 
        parent = [i for i in range(tot)]
        def find(root):
            if root != parent[root]:
                parent[root] = find(parent[root])
            return parent[root]

        def connect(r1,c1,r2,c2):
            if not (0 <= r1 < row and 0 <= c1 < col and 0 <= r2 < row and 0 <= c2 < col):
                return False
            if not (grid[r1][c1] == 0 and grid[r2][c2] == 0):
                return False
            cur1, cur2 = r1*col+c1, r2*col+c2
            root1 = find(cur1)
            root2 = find(cur2)
            # print(r1,c1,root1,';', r2,c2,root2)
            if root1 != root2:
                if root1 < col or root1 >= col*(row-1):
                    parent[root2] = root1
                elif root2 < col or root2 >= col*(row-1):
                    parent[root1] = root2
                else:
                    parent[root1] = root2
                return (root1 < col and root2 >= col*(row-1)) or (root2 < col and root1 >= col*(row-1))
            return False

        for r in range(row):
            for c in range(col):
                if connect(r,c,r-1,c) or connect(r,c,r,c-1):
                    return n
        for i in range(n)[::-1]:
            r, c = cells[i]
            r -= 1
            c -= 1
            grid[r][c] = 0
            # print(grid)
            for dr, dc in [(0,-1),(0,1),(-1,0),(1,0)]:
                dr += r 
                dc += c  
                if connect(r,c,dr,dc):
                    return i  
        return -1



class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0]*col for _ in range(row)]
        n = len(cells)
        
        # print(grid)
        tot = row*col 
        parent = [i for i in range(tot)]
        def find(root):
            if root != parent[root]:
                parent[root] = find(parent[root])
            return parent[root]

        def connect(r1,c1,r2,c2):
            if not (0 <= r1 < row and 0 <= c1 < col and 0 <= r2 < row and 0 <= c2 < col):
                return False
            if not (grid[r1][c1] == 1 and grid[r2][c2] == 1):
                return False
            cur1, cur2 = r1*col+c1, r2*col+c2
            root1 = find(cur1)
            root2 = find(cur2)
            # print(r1,c1,root1,';', r2,c2,root2)
            if root1 != root2:
                if root1%col == 0 or root1%col == col-1:
                    parent[root2] = root1
                elif root2%col == 0 or root2%col == col-1:
                    parent[root1] = root2
                else:
                    parent[root1] = root2
                return (root1%col == 0 and root2%col == col-1) or (root1%col == col-1 and root2%col == 0)
            return False

        for i, (r, c) in enumerate(cells):
            r -= 1
            c -= 1
            grid[r][c] = 1
            for dr, dc in [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,1),(-1,1),(1,-1)]:
                dr += r 
                dc += c  
                if connect(r,c,dr,dc):
                    return i  
            
        return -1


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # 正序，从左至右，八连通
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        # 最左侧出发可连通水域
        visited = set()
        # 最左侧出发暂未连通水域
        wait = set()
        # 增加连通水域，根据九宫格dfs
        def dfs(x, y):
            if y == col:
                return True
            for xx, yy in dirs:
                new_x, new_y = x + xx, y + yy
                if (new_x, new_y) in wait:
                    wait.remove((new_x, new_y))
                    visited.add((new_x, new_y))
                    if dfs(new_x, new_y):
                        return True
            return False
        # 依此遍历cells
        for i, (x, y) in enumerate(cells):
            flag = False
            # 最左侧出发
            if y == 1:
                flag = True
            # 非最左侧，根据九宫格判断能否连通
            else:
                for xx, yy in dirs:
                    new_x, new_y = x + xx, y + yy
                    if (new_x, new_y) in visited:
                        flag = True
                        break
            # 若当前水域可连通，则通过dfs尝试取出wait内的水域
            if flag:
                visited.add((x, y))
                if dfs(x, y):
                    return i
            # 暂未连通，丢入wait
            else:
                wait.add((x, y))


作者：half-empty
链接：https://leetcode-cn.com/problems/last-day-where-you-can-still-cross/solution/onzheng-xu-bian-li-si-lu-by-half-empty-9ko3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。