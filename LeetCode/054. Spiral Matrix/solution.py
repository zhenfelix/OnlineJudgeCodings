class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        n, m = len(matrix), len(matrix[0])
        res, idx = [], 0
        r, c = 0, 0
        while idx < n*m:
            while idx < n*m and c < m and matrix[r][c] != None:
                res.append(matrix[r][c])
                matrix[r][c] = None
                idx += 1
                c += 1
            r += 1
            c -= 1
            while idx < n*m and r < n and matrix[r][c] != None:
                res.append(matrix[r][c])
                matrix[r][c] = None
                idx += 1
                r += 1
            r -= 1
            c -= 1
            while idx < n*m and c >= 0 and matrix[r][c] != None:
                res.append(matrix[r][c])
                matrix[r][c] = None
                idx += 1
                c -= 1
            r -= 1
            c += 1
            while idx < n*m and r >= 0 and matrix[r][c] != None:
                res.append(matrix[r][c])
                matrix[r][c] = None
                idx += 1
                r -= 1
            r += 1
            c += 1
        return res