# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         if len(intervals) < 2:
#             return intervals
#         intervals.sort(key = lambda x: (x[0], x[1]))
#         intervals.append([float('inf'),float('inf')])
#         res = []
#         left, right = intervals[0][0], intervals[0][1]
#         for e in intervals:
#             if e[0] > right:
#                 res.append([left,right])
#                 left, right = e[0], e[1]
#             else:
#                 right = max(right, e[1])
#         return res

class Solution:
	def merge(self, intervals):
	    out = []
	    for e in sorted(intervals, key=lambda i: i[0]):
	        if out and e[0] <= out[-1][-1]:
	            out[-1][-1] = max(out[-1][-1], e[-1])
	        else:
	            out += e,
	    return out

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[1])
        st = [[-float('inf'), -float('inf')]]
        for s, e in intervals:
            while st and s <= st[-1][-1]:
                pre, _ = st.pop()
                s = min(s,pre)
            st.append([s,e])
            
        return st[1:]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        points = []

        for s, e in intervals:
            points.append([s,1])
            points.append([e,-1])
        points.sort(key = lambda x: (x[0],-x[1]))
        cnt = 0
        for p, delta in points:
            cnt += delta
            if cnt == 1 and delta > 0:
                res.append([p])
            elif cnt == 0:
                res[-1].append(p)
        return res 


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort(key = lambda x: (x[1],x[0]))
#         st = []
#         for s, e in intervals:
#             if not st or s > st[-1][-1]:
#                 st.append([s, e])
#             else:
#                 while st and s <= st[-1][-1]:
#                     start, _ = st.pop()
#                 st.append([min(s,start),e])
#         return st 