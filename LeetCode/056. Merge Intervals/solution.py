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