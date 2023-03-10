class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left, right = [0]+nums[:-1], nums[1:]+[0]
        n = len(nums)
        for i in range(1,n):
            left[i] += left[i-1]
        for i in range(n-1)[::-1]:
            right[i] += right[i+1]
        ans = [0]*n 
        for i in range(n):
            ans[i] = abs(left[i]-right[i])
        return ans 