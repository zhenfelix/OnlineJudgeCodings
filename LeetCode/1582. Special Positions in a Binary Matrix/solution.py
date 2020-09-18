class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rows = [sum(mat[i][j] for j in range(m)) for i in range(n)]
        cols = [sum(mat[i][j] for i in range(n)) for j in range(m)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    cnt += 1
        return cnt