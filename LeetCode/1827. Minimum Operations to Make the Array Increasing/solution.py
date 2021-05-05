class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt, n = 0, len(nums)
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                cnt += nums[i-1]+1-nums[i]
                nums[i] = nums[i-1]+1
        return cnt