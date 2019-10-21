# class Solution:
#     def videoStitching(self, clips: List[List[int]], T: int) -> int:
#         n = len(clips)
#         clips = sorted(clips)
#         dp = [float('inf')] * 101
#         dp[0] = 0
#         for start, end in clips:
#             for i in range(start, end+1):
#                 dp[i] = min(dp[i], dp[start]+1)
#         if dp[T] == float('inf'):
#             return -1
#         return dp[T]


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips = sorted(clips)
        start, end, res = 0, 0, 0
        for clip in clips:
            if clip[0] <= start:
                end = max(end, clip[1])
            elif clip[0] > end:
                break
            else:
                start = end
                end = max(end, clip[1])
                res += 1
            if end >= T:
                return res+1
        return -1