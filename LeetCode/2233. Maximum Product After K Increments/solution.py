class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            cur = heapq.heappop(nums)
            heapq.heappush(nums,cur+1)
        ans = 1
        MOD = 10**9+7
        for x in nums:
            ans *= x
            ans %= MOD
        return ans