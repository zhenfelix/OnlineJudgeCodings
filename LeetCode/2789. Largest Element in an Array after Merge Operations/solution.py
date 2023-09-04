class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[-1]
        for i in range(n-1)[::-1]:
            if nums[i] <= nums[i+1]:
                nums[i] += nums[i+1]
            ans = max(ans,nums[i])
        return ans 