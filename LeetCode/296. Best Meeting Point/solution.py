class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        rows = [sum([grid[i][j] for j in range(m)]) for i in range(n)]
        cols = [sum([grid[i][j] for i in range(n)]) for j in range(m)]
        # print(rows)
        # print(cols)
        # x = sum([i*rows[i] for i in range(n)])//sum(rows)
        # if x+1 < n: x = max([x, x+1], key = lambda i: rows[i])
        # y = sum([j*cols[j] for j in range(m)])//sum(cols)
        # if y+1 < m: y = max([y, y+1], key = lambda j: cols[j])
        res = 0
        left, right, cursum = 0, sum(rows), sum([rows[i]*(i+1) for i in range(n)])
        for i in range(n):
            if left - right >= 0:
                break
            cursum = cursum + left - right
            right -= rows[i]
            left += rows[i]
        res += cursum

        left, right, cursum = 0, sum(cols), sum([cols[j]*(j+1) for j in range(m)])
        for j in range(m):
            if left - right >= 0:
                break
            cursum = cursum + left - right
            right -= cols[j]
            left += cols[j]
        res += cursum

        return res