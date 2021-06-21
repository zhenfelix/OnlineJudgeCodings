# class Solution:
#     def minWastedSpace(self, A, boxes):
#         A.sort()
#         res = float('inf')
#         for B in boxes:
#             B.sort()
#             if B[-1] < A[-1]: continue
#             cur = i = 0
#             for b in B:
#                 j = bisect.bisect(A, b, i)
#                 cur += b * (j - i)
#                 i = j
#             res = min(res, cur)
#         return (res - sum(A)) % (10**9 + 7) if res < float('inf') else -1        

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10**9+7
        maxn = 10**5+5
        presums = [0]*maxn
        precnt = [0]*maxn
        n = len(packages)
        heapq.heapify(packages)
        for i in range(1,maxn):
            presums[i] = presums[i-1]
            precnt[i] = precnt[i-1]
            while packages and packages[0] == i:
                presums[i] += packages[0]
                heapq.heappop(packages)
                precnt[i] += 1  
        res = float('inf')
        for box in boxes:
            cur, sums, cnt = 0, 0, 0 
            for b in sorted(box):
                cur += b*(precnt[b]-cnt)-(presums[b]-sums)
                sums = presums[b]
                cnt = precnt[b]
            if cnt < n:
                continue
            res = min(res, cur)
        return -1 if res == float('inf') else (res%MOD)

