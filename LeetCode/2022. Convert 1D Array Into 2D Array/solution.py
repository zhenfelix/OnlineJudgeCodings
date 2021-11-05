class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        sz = len(original)
        if sz != m*n:
            return []
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = original[i*n+j]
        return res