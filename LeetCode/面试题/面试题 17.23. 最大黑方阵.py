class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        n, m = len(matrix), len(matrix[0])
        vertical, horizontal = [[0]*m for _ in range(n)], [[0]*m for _ in range(n)]
        for i in range(n)[::-1]:
            for j in range(m)[::-1]:
                if matrix[i][j] == 0:
                    vertical[i][j], horizontal[i][j] = 1, 1
                    vertical[i][j] += vertical[i+1][j] if i+1 < n else 0
                    horizontal[i][j] += horizontal[i][j+1] if j+1 < m else 0

        r, c, sz = -1, -1, 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for k in range(sz+1,min(vertical[i][j],horizontal[i][j])+1)[::-1]:
                        if horizontal[i+k-1][j] >= k and vertical[i][j+k-1] >= k:
                            r, c, sz = i, j, k
                            break
                        
        return [r,c,sz] if sz > 0 else []



