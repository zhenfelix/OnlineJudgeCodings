class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n, res = len(nums), []
        q = deque()
        for i in range(n):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i-q[0]+1 > k:
                q.popleft()
            if i+1 >= k:
                res.append(nums[q[0]])
        return res
            