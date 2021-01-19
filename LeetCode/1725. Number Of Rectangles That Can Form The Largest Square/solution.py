class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        arr = [min(a,b) for a, b in rectangles]
        return sum(x == max(arr) for x in arr)