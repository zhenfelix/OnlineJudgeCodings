# class Solution:
#     def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
#         n = len(points)
#         res = set()
#         start = cur = min(range(n), key = lambda x: points[x][0])
#         res.add(cur)
#         while len(res) < n:
#             pre = cur
#             cur = (pre+1)%n
#             for i in range(n):
#                 if i in [pre,cur]:
#                     continue
#                 x1, y1 = points[cur][0]-points[pre][0], points[cur][1]-points[pre][1]
#                 x2, y2 = points[i][0]-points[cur][0], points[i][1]-points[cur][1]
#                 cross = x1*y2-x2*y1
#                 if cross > 0:
#                     cur = i
#                 elif cross == 0:
#                     if x1*x2+y1*y2 < 0 and i not in res:
#                         cur = i

#             if cur == start:
#                 break
#             res.add(cur)
#             # print(list(map(lambda x: points[x], res)))
#         return list(map(lambda x: points[x], res))

class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        def cmp(a, b):
            x, y = b[0]-a[0], b[1]-a[1]
            k, d = -float('inf'), 0
            if x == 0:
                k, d = float('inf'), -y
            else:
                k, d = y/x, x 
            return k, d

        def cross(a, b, c):
            x1, y1 = b[0]-a[0], b[1]-a[1]
            x2, y2 = c[0]-b[0], c[1]-b[1]
            return x1*y2-x2*y1 < 0

        n = len(points)
        start = min(range(n), key = lambda i: (points[i][0],points[i][1]))
        st = [points[start]]
        points = sorted(points, key = lambda point: cmp(points[start], point))
        # print(points)
        j = n-2
        while j > 0 and points[j][0] != points[-1][0] and cross(points[-1], points[j], points[j-1]) == 0:
            j -= 1
        # print(n,j)
        points = points[:j] + points[j:n-1][::-1]
        # print(points)
        # print(st)
        for i, point in enumerate(points):
            # if point == st[0]:
            #     continue
            while len(st) > 1 and cross(st[-2], st[-1], point):
                st.pop()
            st.append(point)
            # print(st)
        return st

        

