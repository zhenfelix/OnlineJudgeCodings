class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        n = len(nums)
        if n == 1:
            return nums[0] if k%2 == 0 else -1
        if k == 1:
            return nums[1]
        elif k < n:
            return max(max(nums[:k-1]),nums[k])
        else:
            return max(nums[:k-1])