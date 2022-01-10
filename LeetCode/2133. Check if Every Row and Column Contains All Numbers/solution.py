class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        
        for i in range(n):
            row = [False]*(n+1)
            col = [False]*(n+1)
            for j in range(n):
                r = matrix[i][j]
                c = matrix[j][i]
                if row[r] or col[c]:
                    return False
                row[r] = True
                col[c] = True
        return True
