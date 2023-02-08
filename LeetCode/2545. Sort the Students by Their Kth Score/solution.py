class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(score), len(score[0])
        idx = list(range(n))
        s = [score[i][k] for i in range(n)]
        idx.sort(key = lambda x: -s[x])
        mat = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                mat[i][j] = score[idx[i]][j]
        return mat