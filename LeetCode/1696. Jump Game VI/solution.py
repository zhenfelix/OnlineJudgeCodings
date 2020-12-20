class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-float('inf')]*n 
        dp[0] = nums[0]
        q = deque()
        q.append(0)
        for i in range(1,n):
            while i-q[0] > k:
                q.popleft()
            dp[i] = dp[q[0]] + nums[i]
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            q.append(i)
        return dp[-1]