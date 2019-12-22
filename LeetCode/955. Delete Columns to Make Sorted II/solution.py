
class Solution:
#     def minDeletionSize(self, A: List[str]) -> int:
#         n, m = len(A), len(A[0])
#         cmp = set()
#         cnt = 0
#         for j in range(m):
#             print(cmp)
#             if len(cmp) >= n-1:
#                 break
#             if any((i,i+1) not in cmp and A[i][j]>A[i+1][j] for i in range(n-1)):
#                 cnt += 1
#             else:
#                 [cmp.add((i,i+1)) for i in range(n-1) if A[i][j]<A[i+1][j]]
#         return cnt
                   

    
    def minDeletionSize(self, A):
        res, n, m = 0, len(A), len(A[0])
        is_sorted = [0] * (n - 1)
        for j in range(m):
            is_sorted2 = is_sorted[:]
            for i in range(n - 1):
                if A[i][j] > A[i + 1][j] and is_sorted[i] == 0:
                    res += 1
                    break
                is_sorted2[i] |= A[i][j] < A[i + 1][j]
            else i == n-1:
                is_sorted = is_sorted2
        return res