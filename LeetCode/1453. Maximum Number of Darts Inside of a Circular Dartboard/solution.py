# class Solution:
#     def numPoints(self, points: List[List[int]], r: int) -> int:
#         epsilon = 10**-6
#         def distance2(x1,y1,x2,y2):
#             return (x1-x2)**2 + (y1-y2)**2

#         def center(x1,y1,x2,y2):
#             d2 = distance2(x1,y1,x2,y2)
#             # print('d',d)
#             x0, y0 = (x1+x2)/2, (y1+y2)/2
#             if 4*r**2-d2 < 0: return []
#             h = (r**2-d2/4)**0.5
#             return [(x0+h*(y1-y2)/d2**0.5,y0-h*(x1-x2)/d2**0.5),(x0-h*(y1-y2)/d2**0.5,y0+h*(x1-x2)/d2**0.5)]

#         res, n, cs = 1, len(points), []
#         for i in range(n):
#             sums = 0
#             for j in range(i+1,n):
#                 cs += center(points[i][0],points[i][1],points[j][0],points[j][1])
#         # print(cs)
#         for x, y in cs:
#             cnt = sum(distance2(x,y,points[i][0],points[i][1]) <= r**2+epsilon for i in range(n))
#             res = max(res,cnt)
#         return res

    def numPoints(self, A, r):
        res = 1
        for (x1, y1), (x2, y2) in itertools.combinations(A, 2):
            d = ((x1 - x2)**2 + (y1 - y2)**2) / 4.0
            if d > r * r: continue
            x0 = (x1 + x2) / 2.0 + (y2 - y1) * (r * r - d)**0.5 / (d * 4) ** 0.5
            y0 = (y1 + y2) / 2.0 - (x2 - x1) * (r * r - d)**0.5 / (d * 4) ** 0.5
            res = max(res, sum((x - x0)**2 + (y - y0)**2 <= r * r + 0.00001 for x, y in A))

        return res

class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        ans = 0
        for x, y in points: 
            angles = []
            for x1, y1 in points: 
                if (x1 != x or y1 != y) and (d:=sqrt((x1-x)**2 + (y1-y)**2)) <= 2*r: 
                    angle = atan2(y1-y, x1-x)
                    delta = acos(d/(2*r))
                    angles.append((angle-delta, +1)) #entry, entry angle is always smaller
                    angles.append((angle+delta, -1)) #exit
            angles.sort(key=lambda x: (x[0], -x[1]))
            # print(min(angles),max(angles))
            print(angles)
            val = 0
            for _, entry in angles: 
                # val += entry
                # val = max(val, 0)
                # ans = max(ans, val)
                ans = max(ans, val := val+entry)
                # print(val)
        return ans + 1