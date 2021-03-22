class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(0)
        cur, res = 0, 0
        for i in range(n):
            if nums[i] <= nums[i-1]:
                cur = 0

            cur += nums[i]
            res = max(res, cur)
        return res 