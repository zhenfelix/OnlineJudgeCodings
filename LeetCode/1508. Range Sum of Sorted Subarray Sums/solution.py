class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        q = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(q)
        res = 0
        for i in range(right):
            cur, idx = heapq.heappop(q)
            if i >= left-1:
                res += cur
                res %= (10**9+7)
            idx += 1
            if idx < n:
                heapq.heappush(q,(cur+nums[idx],idx))
        return res
