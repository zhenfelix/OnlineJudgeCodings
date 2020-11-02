class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = [point[0] for point in points]
        points.sort()
        n = len(points)
        res = 0
        for i in range(1,n):
            res = max(res, points[i]-points[i-1])
        return res