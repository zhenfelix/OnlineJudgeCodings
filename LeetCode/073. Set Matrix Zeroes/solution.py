class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            flag = False
            for j in range(m):
                if matrix[i][j] == 0:
                    flag = True
                    break
            if flag:
                for j in range(m):
                    matrix[i][j] = float('inf') if matrix[i][j] != 0 else 0
        for j in range(m):
            flag = False
            for i in range(n):
                if matrix[i][j] == 0:
                    flag = True
                    break
            if flag:
                for i in range(n):
                    matrix[i][j] = float('inf') if matrix[i][j] != 0 else 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
