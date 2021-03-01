from functools import lru_cache
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # events = [[s-1,e,v] for s,e,v in events]
        events.sort()
        nxt = []
        for i, (s,e,v) in enumerate(events):
            nxt.append(bisect.bisect_left(events,[e+1,e+1,0],lo=i+1,hi=len(events)))
        # print(events)
        @lru_cache(None)
        def dfs(i,r):
            # print(i)
            if i >= len(events) or r <= 0:
                return 0
            s, e, v = events[i]
            # j = bisect.bisect_left(events,[e+1,e+1,0],lo=i+1,hi=len(events))
            j = nxt[i]
            # print(i,j)
            return max(v+dfs(j,r-1),dfs(i+1,r))
        return dfs(0,k)