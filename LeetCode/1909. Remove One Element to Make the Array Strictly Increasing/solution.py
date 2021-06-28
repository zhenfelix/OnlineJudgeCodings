class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if all(a < b for a, b in zip(nums,nums[1:])):
            return True
        n = len(nums)
        for i in range(n):
            arr = nums[:i] + nums[i+1:]
            if all(a < b for a, b in zip(arr, arr[1:])):
                return True
        return False