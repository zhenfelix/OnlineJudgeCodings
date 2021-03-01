class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mi, mx, res = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            mi, mx = min(mi*nums[i],mx*nums[i],nums[i]), max(mi*nums[i],mx*nums[i],nums[i])
            res = max(res, mx)
        return res 