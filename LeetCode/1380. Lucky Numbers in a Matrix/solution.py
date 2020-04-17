class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        rows = [min(matrix[i][j] for j in range(m)) for i in range(n)]
        cols = [max(matrix[i][j] for i in range(n)) for j in range(m)]
        return [matrix[i][j] for i in range(n) for j in range(m) if rows[i] == cols[j]]