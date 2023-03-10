class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        nums = [-x for x in nums]
        heapify(nums)
        for _ in range(k):
            x = -heappop(nums)
            ans += x  
            x = (x-1)//3+1
            heappush(nums, -x)
        return ans 