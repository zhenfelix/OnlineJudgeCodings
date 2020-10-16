class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        mx, q = -float('inf'), []
        res = [-float('inf'), float('inf')]
        for i, arr in enumerate(nums):
            mx = max(mx, arr[0])
            q.append((arr[0],i,0))
        heapq.heapify(q)
        while q:
            val, i, j = heapq.heappop(q)
            if mx - val < res[-1] - res[0]:
                res = [val, mx]
            if j + 1 >= len(nums[i]):
                break
            mx = max(mx, nums[i][j+1])
            heapq.heappush(q, (nums[i][j+1],i,j+1))
        return res
