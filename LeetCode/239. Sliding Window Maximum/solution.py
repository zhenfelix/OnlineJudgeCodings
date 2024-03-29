from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        for i, x in enumerate(nums):
            # print(dq)
            if len(dq) > 0 and i-dq[0] == k:
                dq.popleft()
            while len(dq) > 0 and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                ans.append(nums[dq[0]])
        return ans
                

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            if i-q[0] >= k:
                q.popleft()
            if i >= k-1:
                res.append(nums[q[0]])
        return res