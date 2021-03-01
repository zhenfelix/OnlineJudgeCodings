from functools import reduce
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        cnt, res = 0, 0
        intervals = [[(x[0],1),(x[1],-1)] for x in intervals]
        intervals = reduce(lambda a,b:a+b, intervals, [])
        # print(intervals)
        intervals.sort()
        for time, delta in intervals:
            cnt += delta
            res = max(res, cnt)
        return res




import heapq
from typing import *
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# class Solution:
#     """
#     @param intervals: an array of meeting time intervals
#     @return: the minimum number of conference rooms required
#     """
#     def minMeetingRooms(self, intervals):
#         # Write your code here
#         intervals.sort(key=lambda x: x.start)
#         q = []
#         res = 0
#         for x in intervals:
#             start, end = x.start, x.end
#             while q and q[0] <= start:
#                 heapq.heappop(q)
#             heapq.heappush(q,end)
#             res = max(res,len(q))
#         return res

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        intervals.sort(key=lambda x: x.start)
        q = []
        for x in intervals:
            start, end = x.start, x.end
            if q and q[0] <= start: #think it as a sliding window
                heapq.heappop(q)
            heapq.heappush(q,end)
        return len(q)


import heapq
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        intervals.sort(key=lambda x: x.start)
        q, res = [], 0
        for x in intervals:
            start, end = x.start, x.end
            heapq.heappush(q,end)
            while q[0] <= start: #think it as a sliding window
                heapq.heappop(q)
            res = max(res,len(q))
        return res
