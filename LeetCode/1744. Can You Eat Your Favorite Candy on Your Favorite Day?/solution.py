class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(candiesCount)
        for i in range(1,n):
            candiesCount[i] += candiesCount[i-1]
        res = []
        for kind, day, cap in queries:
            day += 1
            lo, hi = day, day*cap
            left = bisect.bisect_left(candiesCount, lo)
            right = bisect.bisect_left(candiesCount, hi)
            # print(left,right,candiesCount[left:right+1])
            if left <= kind <= right:
                res.append(True)
            else:
                res.append(False)
        return res 


class Solution:
    def canEat(self, candiesCount, queries):
        A = [0] + list(accumulate(candiesCount))
        return [A[t] // c <= d < A[t + 1] for t, d, c in queries]        