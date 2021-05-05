class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for x, y, r in queries:
            cnt = sum((x-a)**2+(y-b)**2 <= r**2 for a, b in points)
            ans.append(cnt)
        return ans