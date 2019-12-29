class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[1], x[0]))
        # print(points)
        cnt, cur = 0, -float("inf")
        for s, e in points:
            if s > cur:
                cur = e 
                cnt += 1
        return cnt 