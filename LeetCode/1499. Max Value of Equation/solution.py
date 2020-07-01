class Solution:
#     def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
#         j, n = 1, len(points)
#         q = deque()
#         res = -float('inf')
#         for i in range(n-1):
#             j = max(j,i+1)
#             if q and i == q[0]:
#                 q.popleft()
#             while j < n and points[j][0]-points[i][0] <= k:
#                 while q and points[q[-1]][-1] + points[q[-1]][0] < points[j][-1] + points[j][0]:
#                     q.pop()
#                 q.append(j)
#                 j += 1
            
#             if q:
#                 res = max(res, points[i][-1]-points[i][0]+points[q[0]][-1]+points[q[0]][0])
#             # print(i,q,res)
#         return res


    def findMaxValueOfEquation(self, A, k):
        q = collections.deque()
        res = -float('inf')
        for x, y in A:
            while q and q[0][1] < x - k:
                q.popleft()
            if q: res = max(res, q[0][0] + y + x)
            while q and q[-1][0] <= y - x:
                q.pop()
            q.append([y - x, x])
        return res

