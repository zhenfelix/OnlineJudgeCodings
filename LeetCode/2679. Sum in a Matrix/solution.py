class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        n = len(nums)
        m = len(nums[0])
        for i in range(n):
            nums[i].sort(reverse = True)
        ans = 0
        for j in range(m):
            ans += max(nums[i][j] for i in range(n))
        return ans 