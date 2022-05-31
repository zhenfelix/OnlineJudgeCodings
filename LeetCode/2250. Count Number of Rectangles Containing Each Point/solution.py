class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort()
        mh = max(h for l, h in rectangles)
        ls = [[l for l, h in rectangles]]
        for hy in range(1,mh+1):
            ls.append([])
            for l, h in rectangles:
                if h >= hy:
                    ls[-1].append(l)
            # print(ls)
        ans = [0]*len(points)
        # print(ls)
        for i, (x, y) in enumerate(points):
            if y <= mh:
                cnt = bisect.bisect_left(ls[y], x)
                ans[i] = (len(ls[y])-cnt)
        return ans


from sortedcontainers import *
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        m = len(points)
        ans = [0]*m 
        idx = list(range(m))
        idx.sort(key = lambda x: -points[x][-1])
        rectangles.sort(key = lambda x: x[-1])
        ls = SortedList()
        for i in idx:
            x, y = points[i]
            while rectangles and rectangles[-1][-1] >= y:
                l, h = rectangles.pop()
                ls.add(l)
            cnt = ls.bisect_left(x)
            ans[i] = len(ls)-cnt
        return ans