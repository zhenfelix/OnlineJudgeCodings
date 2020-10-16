class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        res = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                cur = min(rowSum[i],colSum[j])
                rowSum[i] -= cur
                colSum[j] -= cur
                res[i][j] = cur
        return res