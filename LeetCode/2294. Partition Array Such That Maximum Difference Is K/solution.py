class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        cnt = 1
        pre = 0
        nums.sort()
        for cur in range(len(nums)):
            if nums[cur] - nums[pre] > k:
                cnt += 1
                pre = cur
        return cnt
