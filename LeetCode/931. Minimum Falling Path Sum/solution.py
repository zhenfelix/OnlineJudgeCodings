class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        for i in range(1,n):
            A[i-1].append(float('inf'))
            for j in range(n):
                A[i][j] += min(A[i-1][k] for k in [j-1,j,j+1])
        return min(A[-1][:])
