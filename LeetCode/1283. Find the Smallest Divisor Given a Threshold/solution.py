
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left <= right:
            mid = (left+right)//2
            # if sum(map(lambda x: (x-1)//mid+1, nums)) > threshold:
            if sum((x-1)//mid+1 for x in nums) > threshold:
                left = mid + 1
            else:
                right = mid - 1
        return left