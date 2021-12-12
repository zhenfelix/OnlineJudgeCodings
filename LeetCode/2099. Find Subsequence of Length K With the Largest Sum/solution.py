class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        q = [(-nums[i],i) for i in range(n-k)]
        heapq.heapify(q)
        for i in range(n-k,n):
            heapq.heappush(q, (-nums[i],i))
            v, j = heapq.heappop(q)
            res.append(j)
        return [nums[j] for j in sorted(res)]


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = sorted([(x,i) for i, x in enumerate(nums)])[-k:]
        arr = sorted([i for x, i in arr])
        return [nums[i] for i in arr]