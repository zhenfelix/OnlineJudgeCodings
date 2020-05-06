# class Solution:
#     def kthSmallest(self, mat: List[List[int]], k: int) -> int:
#         n, m = len(mat), len(mat[0])
#         sums = [0]
#         for row in mat:
#             sums = [s+r for s in sums for r in row]
#             heapq.heapify(sums)
#             tmp = []
#             for _ in range(k):
#                 if not sums:
#                     break
#                 tmp.append(heapq.heappop(sums))
#             sums = tmp
#         return sums[-1]

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        n, m = len(mat), len(mat[0])
        sums = [0]
        for row in mat:
            sums = self.kthPair(sums,row,k)
        return sums[-1]

    def kthPair(self, A, B, k):
        if A and B and k:
            res = []
            dp = [(A[0]+B[j],0,j) for j in range(len(B))]
            heapq.heapify(dp)
            for _ in range(min(k,len(A)*len(B))):
                cur, i, j = heapq.heappop(dp)
                res.append(cur)
                if i+1 < len(A):
                    heapq.heappush(dp,(A[i+1]+B[j],i+1,j))
            return res
        return []
        
        