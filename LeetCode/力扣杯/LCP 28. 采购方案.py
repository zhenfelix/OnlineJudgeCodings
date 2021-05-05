class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        n, res = len(nums), 0
        left, right = 0, n-1
        while left <= right:
            while left <= right and nums[left] + nums[right] > target:
                right -= 1
            res += max(0, right - left)
            left += 1
        return res%(10**9+7)
