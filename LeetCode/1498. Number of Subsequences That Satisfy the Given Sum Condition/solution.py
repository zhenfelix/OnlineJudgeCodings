class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0] * 2 > target:
            return 0
        left = 0
        right = len(nums) - 1
        res = 0
        mode = 1_0000_0000_7
        while left <= right:
            if nums[left] + nums[right] <= target:
                res += (1 << (right-left))
                res %= mode
                left += 1
            else:
                right -= 1
        return res
