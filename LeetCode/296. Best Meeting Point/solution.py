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



# from math import inf
# class Solution:
#     def minTotalDistance(self, cnts: List[List[int]]) -> int:
#         n, m = len(cnts), len(cnts[0])
#         sums = [[0]*m for _ in range(n)]
#         ans = inf
#         for j in range(m):
#             for i in range(1,n):
#                 sums[i][j] = cnts[i][j]*i + sums[i-1][j]
#                 cnts[i][j] += cnts[i-1][j]
#         # print(sums)
#         # print(cnts)
#         for row in range(n):
#             c = [cnts[-1][col] for col in range(m)]
#             s = [cnts[row][col]*row-sums[row][col]+sums[-1][col]-sums[row][col]-(cnts[-1][col]-cnts[row][col])*row for col in range(m)]
#             cs = [0]*m
#             # print(row,c,s)
#             for j in range(1,m):
#                 cs[j] = cs[j-1] + c[j]*j
#                 s[j] += s[j-1]
#                 c[j] += c[j-1]
#             for j in range(m):
#                 left = s[j] + c[j]*j - cs[j]
#                 right = s[-1]-s[j] + cs[-1]-cs[j]-(c[-1]-c[j])*j
#                 # print(row,j,left,right)
#                 ans = min(ans, left+right)
#         return ans