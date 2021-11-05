class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        intervals = []
        for i, e in enumerate(events):
            start, end, val = e
            intervals.append((start-1,i+1))
            intervals.append((end,-i-1))
        intervals.sort()
        n = len(intervals)
        left, right = [0]*n, [0]*n
        mx = 0
        for i in range(n):
            t, idx = intervals[i]
            if idx < 0:
                mx = max(mx, events[-idx-1][-1])
            left[i] = mx 
        mx = 0
        for i in range(n)[::-1]:
            t, idx = intervals[i]
            if idx > 0:
                mx = max(mx, events[idx-1][-1])
            right[i] = mx 
        res = 0
        for i in range(n):
            res = max(res, left[i]+right[i])
        return res


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events = [(s-1,e,v) for s,e,v in events]
        events.sort()
        res, mx = 0, 0
        left, right = [], []
        for i, (s,e,v) in enumerate(events):
            right.append((-v,i))
        heapq.heapify(right)
        for i, (s,e,v) in enumerate(events): 
            while right and right[0][-1] < i:
                heapq.heappop(right)
            while left and left[0][0] <= s:
                t, vv = heapq.heappop(left)
                mx = max(mx, vv)
            res = max(res, mx-right[0][0])
            heapq.heappush(left, (e,v))
        return res



class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events = [(s-1,e,v) for s,e,v in events]
        events.sort()
        res, mx = 0, 0
        pq = []
        for i, (s,e,v) in enumerate(events): 
            while pq and pq[0][0] <= s:
                t, vv = heapq.heappop(pq)
                mx = max(mx, vv)
            res = max(res, mx+v)
            heapq.heappush(pq, (e,v))
        return res