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