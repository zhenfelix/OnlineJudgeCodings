class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0: return False
        n = len(grid)
        arr = []
        for i in range(n):
            for j in range(n):
                arr.append((grid[i][j],i,j))
        arr.sort()
        for i in range(1,n*n):
            dx = abs(arr[i][1]-arr[i-1][1])
            dy = abs(arr[i][2]-arr[i-1][2])
            if not (dx and dy and dx+dy == 3):
                return False
        return True


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        pos = [0] * (len(grid) ** 2)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                pos[x] = (i, j)  # 记录坐标
        if pos[0] != (0, 0):  # 必须从左上角出发
            return False
        for (i, j), (x, y) in pairwise(pos):
            dx, dy = abs(x - i), abs(y - j)  # 移动距离
            if (dx != 2 or dy != 1) and (dx != 1 or dy != 2):  # 不合法
                return False
        return True


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/4MTE6Z/view/vBpzpM/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。