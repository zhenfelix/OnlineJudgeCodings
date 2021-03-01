class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key = lambda x: (x[1],-x[0]))
        intervals.sort(key = lambda x: x[1])
        # intervals.sort(key = lambda x: (x[1],x[0]))
        # print(intervals)
        cnt, cur = 0, -float("inf")
        for s, e in intervals:
            if s < cur:
                cnt += 1
            else:
                cur = e 
        return cnt



class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        cnt, cur = 0, -float("inf")
        for s, e in intervals:
            if s < cur:
                cnt += 1
                cur = min(cur,e) 
            else:
                cur = e
        return cnt