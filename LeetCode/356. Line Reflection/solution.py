
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        left, right = float('inf'), -float('inf')
        seen = set()
        for point in points:
            x, y = point[0], point[1]
            left = min(left,x)
            right = max(right,x)
            seen.add((x,y))
        mid = (left+right)
        for point in points:
            x, y = point[0], point[1]
            if (mid-x,y) not in seen:
                return False
        return True