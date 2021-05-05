class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res, cnt, sums, n, left = 0, 0, 0, len(nums), 0
        nums.sort()
        pre = nums[0]
        for right in range(n):
            sums += cnt*(nums[right]-pre)
            pre = nums[right]
            cnt += 1
            while sums > k:
                sums -= (nums[right]-nums[left])
                cnt -= 1
                left += 1
            res = max(res, cnt)
        return res
