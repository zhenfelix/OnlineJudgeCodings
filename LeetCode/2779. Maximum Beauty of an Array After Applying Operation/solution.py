class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        j = 0
        ans = 0
        for i in range(n):
            while nums[i]-nums[j] > k*2:
                j += 1
            ans = max(ans, i-j+1)
        return ans 