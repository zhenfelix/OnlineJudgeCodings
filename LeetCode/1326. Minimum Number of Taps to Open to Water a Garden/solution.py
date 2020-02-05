# class Solution:
#     def minTaps(self, n: int, ranges: List[int]) -> int:
#         intervals = [[i-radius, i+radius] for i, radius in enumerate(ranges)]
#         intervals.sort()
#         dp = [float('inf')]*(n+1)
#         dp[0] = 0
#         for a, b in intervals:
#             a = max(a,0)
#             b = min(b,n)
#             for i in range(a,b+1):
#                 dp[i] = min(dp[i],dp[a]+1)
#         if dp[n] == float('inf'):
#             return -1
#         return dp[n]


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = [[i-radius, i+radius] for i, radius in enumerate(ranges)]
        intervals.sort()
        m = len(intervals)
        cur, reach, cnt = 0, 0, 0
        while reach < n:
            tmp = reach
            if cur >= m or intervals[cur][0] > tmp:
                return -1
            while cur < m and intervals[cur][0] <= tmp:
                reach = max(reach, intervals[cur][1])
                cur += 1
            cnt += 1
        return cnt
