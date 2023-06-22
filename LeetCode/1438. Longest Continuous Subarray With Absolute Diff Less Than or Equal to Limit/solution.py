# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         maxq, minq = deque(), deque()
#         left, res = 0, 0
#         for right, num in enumerate(nums):
#             while maxq and nums[maxq[-1]] <= num:
#                 maxq.pop()
#             maxq.append(right)
#             while minq and nums[minq[-1]] >= num:
#                 minq.pop()
#             minq.append(right)
#             while nums[maxq[0]]-nums[minq[0]] > limit:
#                 if left == maxq[0]:
#                     maxq.popleft()
#                 if left == minq[0]:
#                     minq.popleft()
#                 left += 1
#             res = max(res, right-left+1)
#         return res

class Solution:
#     def longestSubarray(self, A, limit):
#         maxq, minq = [], []
#         res = i = 0
#         for j, a in enumerate(A):
#             heapq.heappush(maxq, [-a, j])
#             heapq.heappush(minq, [a, j])
#             while -maxq[0][0] - minq[0][0] > limit:
#                 i = min(maxq[0][1], minq[0][1]) + 1
#                 while maxq[0][1] < i: heapq.heappop(maxq)
#                 while minq[0][1] < i: heapq.heappop(minq)
#             res = max(res, j - i + 1)
#         return res

class Solution:
    def longestSubarray(self, A, limit):
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(A):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            while i <= j:
                while maxq[0][1] < i: heappop(maxq)
                while minq[0][1] < i: heappop(minq)
                if -maxq[0][0] - minq[0][0] <= limit: break
                i += 1
            res = max(res, j - i + 1)
        return res

    def longestSubarray(self, A, limit):
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in A:
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == A[i]: maxd.popleft()
                if mind[0] == A[i]: mind.popleft()
                i += 1
        return len(A) - i