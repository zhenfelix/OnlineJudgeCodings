# class Solution:
#     def minAreaFreeRect(self, points: List[List[int]]) -> float:
#         res = float('inf')
#         n = len(points)
#         s = set([(point[0],point[1]) for point in points])
#         for k in range(n):
#             for i in range(n):
#                 if i == k:
#                     continue
#                 for j in range(i+1,n):
#                     if j == k:
#                         continue
#                     x1, y1 = points[i][0]-points[k][0], points[i][1]-points[k][1]
#                     x2, y2 = points[j][0]-points[k][0], points[j][1]-points[k][1]
#                     if x1*x2+y1*y2 == 0 and (points[k][0]+x1+x2, points[k][1]+y1+y2) in s:
#                         res = min(res, abs(x1*y2-x2*y1))
#         if res == float('inf'):
#             return 0
#         return res


# class Solution:
#     def minAreaFreeRect(self, points: List[List[int]]) -> float:
#         def gcd(a, b):
#             if a < b: a, b = b, a 
#             while b != 0:
#                 a, b = b, a%b
#             return a

#         def length(a, b):
#             return (a**2 + b**2)**(0.5)

#         res = float('inf')
#         allpoints = set([(point[0],point[1]) for point in points])
#         n = len(points)
#         for i in range(n):
#             slopes = collections.defaultdict(list)
#             for j in range(i+1,n):
#                 x, y = points[j][0]-points[i][0], points[j][1]-points[i][1]
#                 xx, yy = x, y
#                 if xx < 0: xx, yy = -xx, -yy
#                 g = gcd(xx,abs(yy))
#                 xx, yy = xx//g, yy//g
#                 if xx == 0: yy = 1
#                 if yy == 0: xx = 1
#                 xp, yp = abs(yy), (xx if yy <= 0 else -xx)
#                 for ex, ey in slopes[xp,yp]:
#                     if (points[i][0]+x+ex, points[i][1]+y+ey) in allpoints:
#                         res = min(res, length(ex,ey)*length(x,y))
#                 # if (xp,yp) in slopes and (points[i][0]+x+slopes[xp,yp][0], points[i][1]+y+slopes[xp,yp][1]) in allpoints:
#                 #     res = min(res, length(slopes[xp,yp][0],slopes[xp,yp][1])*length(x,y))
#                 # if (xx,yy) in slopes and length(slopes[xx,yy][0],slopes[xx,yy][1]) >= length(x,y):
#                 #     continue
#                 slopes[xx,yy].append((x,y))

#         if res == float('inf'):
#             return 0
#         return res


class Solution(object):
    def minAreaFreeRect(self, points):
        points = [complex(*z) for z in points]
        seen = collections.defaultdict(list)
        ans = float("inf")
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            for P_ in seen[center, radius]:
                ans = min(ans, abs(P-P_)*abs(P-(2*center-P_)))
            seen[center, radius].append(P)

        
        # for (center, radius), candidates in seen.items():
        #     for P, Q in itertools.combinations(candidates, 2):
        #         ans = min(ans, abs(P - Q) * abs(P - (2*center - Q)))

        return ans if ans < float("inf") else 0