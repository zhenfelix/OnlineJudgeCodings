class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = nums.copy(), nums.copy()  
        for i in range(1,n):
            left[i] = max(left[i], left[i-1])
        for i in range(n-1)[::-1]:
            right[i] = min(right[i], right[i+1])
        res = 0
        for i in range(1,n-1):
            if nums[i] > left[i-1] and nums[i] < right[i+1]:
                res += 2
            elif nums[i] > nums[i-1] and nums[i] < nums[i+1]:
                res += 1
        return res