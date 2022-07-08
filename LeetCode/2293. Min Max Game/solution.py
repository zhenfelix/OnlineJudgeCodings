class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ans = []
        for i in range(n//2):
            if i%2 == 0:
                ans.append(min(nums[i*2],nums[i*2+1]))
            else:
                ans.append(max(nums[i*2],nums[i*2+1]))
        return self.minMaxGame(ans)