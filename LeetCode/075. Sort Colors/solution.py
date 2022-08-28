class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = j = k = 0
        for k in range(n):
            if nums[k] == 1:
                nums[k], nums[j] = nums[j], nums[k]
                j += 1
            elif nums[k] == 0:
                nums[k], nums[j], nums[i] = nums[j], nums[i], nums[k]
                i += 1
                j += 1
        return 