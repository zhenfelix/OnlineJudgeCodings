class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = []
        ans = -float('inf')
        for i in range(n):
            while dp and i-dp[0][-1] > k:
                heapq.heappop(dp)
            pre = 0
            if dp:
                pre = max(pre, -dp[0][0])
            heapq.heappush(dp,(-pre-nums[i],i))
            ans = max(ans,-dp[0][0])
            # print(dp, ans)
        return ans 


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res = -float('inf')
        q = deque()
        for i, a in enumerate(nums):
            while q and q[0] < i-k:
                q.popleft()
            pre = nums[q[0]] if q else 0
            nums[i] += max(0,pre)
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            res = max(res,nums[i])
        return res



class Solution:
    # def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     q = deque()
    #     for i in range(n):
    #         nums[i] += q[0] if q else 0
    #         if q and i >= k and q[0] == nums[i-k]:
    #             q.popleft()
    #         if nums[i] > 0:
    #             while q and q[-1] < nums[i]:
    #                 q.pop()
    #             q.append(nums[i])
    #     return max(nums) 

    def constrainedSubsetSum(self, A, k):
        deque = collections.deque()
        for i in range(len(A)):
            A[i] += deque[0] if deque else 0
            while len(deque) and A[i] > deque[-1]:
                deque.pop()
            if A[i] > 0:
                deque.append(A[i])
            if i >= k and deque and deque[0] == A[i - k]:
                deque.popleft()
        return max(A)