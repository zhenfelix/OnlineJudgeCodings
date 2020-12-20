class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, cursum, res = 0, 0, 0
        cc = Counter()
        for right in range(n):
            cursum += nums[right]
            cc[nums[right]] += 1
            while cc[nums[right]] > 1:
                cursum -= nums[left]
                cc[nums[left]] -= 1
                left += 1
            res = max(res,cursum)
        return res 