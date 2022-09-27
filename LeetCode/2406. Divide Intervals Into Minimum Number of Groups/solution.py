class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        tails = [-float('inf')]
        for a, b in sorted(intervals):
            t = heappop(tails)
            heappush(tails,b)
            if t >= a:
                heappush(tails,t)
            # print(tails)
        return len(tails)


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        mx = max(c[-1] for c in intervals)
        arr = [0]*(mx+1)
        for a, b in intervals:
            arr[a] += 1
            arr[b+1] -= 1
        cnt, res = 0, 0
        for delta in arr:
            cnt += delta
            res = max(res,cnt)
        return res