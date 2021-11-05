class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        for x, y in points:
            seen.add((x,y))
        n = len(points)
        res = float('inf')
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1,n):
                x2, y2 = points[j]
                if abs(x1-x2) and abs(y1-y2) and (x1,y2) in seen and (x2,y1) in seen:
                    res = min(res, abs((x2-x1)*(y2-y1)))
        return res if res < float('inf') else 0