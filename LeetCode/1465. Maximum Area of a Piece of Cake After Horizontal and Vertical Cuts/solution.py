class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        n, m = len(horizontalCuts), len(verticalCuts)
        hh, vv = 0, 0
        for i in range(1,n):
            hh = max(hh, horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1,m):
            vv = max(vv, verticalCuts[i]-verticalCuts[i-1])
        return (hh*vv)%(10**9+7)