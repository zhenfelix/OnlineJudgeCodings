class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        pre = -1
        ans = 0
        for i in range(n):
            if nums[i] != 0:
                pre = i 
            else:
                ans += i-pre
        return ans
