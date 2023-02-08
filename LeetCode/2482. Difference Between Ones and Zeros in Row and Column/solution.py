class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        ans = [[0]*m for _ in range(n)]
        row = [0]*n 
        col = [0]*m 
        for i in range(n):
            for j in range(m):
                row[i] += grid[i][j]
                col[j] += grid[i][j]
        for i in range(n):
            for j in range(m):
                ans[i][j] = row[i]-(m-row[i])+col[j]-(n-col[j])
        return ans 


class Solution:

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        r = [0] * len(grid)

        c = [0] * len(grid[0])

        for i, row in enumerate(grid):

            for j, x in enumerate(row):

                r[i] += x * 2 - 1

                c[j] += x * 2 - 1  # 1 -> 1, 0 -> -1

        for i, x in enumerate(r):

            for j, y in enumerate(c):

                grid[i][j] = x + y

        return grid

作者：灵茶山艾府
链接：https://leetcode.cn/problems/difference-between-ones-and-zeros-in-row-and-column/solutions/1993060/mo-ni-liang-ge-you-hua-by-endlesscheng-jldf/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。