class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                matrix[i][j] += matrix[i][j-1] if j-1 >= 0 else 0
        sums = -float('inf')
        res = []
        for c1 in range(m):
            for c2 in range(c1,m):
                idx, pre, cur = -1, 0, 0
                for r in range(n):
                    cur += matrix[r][c2]-matrix[r][c1-1] if c1-1 >= 0 else matrix[r][c2]
                    if cur-pre > sums:
                        sums = cur-pre
                        res = [idx+1,c1,r,c2]
                    if cur < pre:
                        idx, pre = r, cur
        return res