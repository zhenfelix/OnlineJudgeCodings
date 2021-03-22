class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        idx, dis = -1, float('inf')
        for i in range(len(points)):
            a, b = points[i]
            if a == x or b == y:
                tmp = abs(a-x) + abs(b-y)
                if tmp < dis:
                    idx, dis = i, tmp
        return idx 