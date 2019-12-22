class Solution:
#     def minDeletionSize(self, A: List[str]) -> int:
#         n, m = len(A), len(A[0])
#         return sum(any(A[i][j]>A[i+1][j] for i in range(n-1)) for j in range(m))

    def minDeletionSize(self, A):
        return sum(any(a > b for a, b in zip(col, col[1:])) for col in zip(*A))