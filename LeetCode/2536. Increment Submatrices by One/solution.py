class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0]*(n+1) for _ in range(n+1)]
        for r1,c1,r2,c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2+1] -= 1
            diff[r2+1][c1] -= 1
            diff[r2+1][c2+1] += 1
        mat = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                mat[i][j] = mat[i-1][j]+mat[i][j-1]-mat[i-1][j-1]+diff[i][j]
        return [mat[i][:n] for i in range(n)]