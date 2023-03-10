class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        ans = 0
        while left < right:
            ans += int(str(nums[left])+str(nums[right]))
            left += 1
            right -= 1
        if left == right:
            ans += nums[left]
        return ans