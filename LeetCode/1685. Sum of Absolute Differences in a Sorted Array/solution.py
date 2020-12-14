class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, sum(nums[i]-nums[0] for i in range(1,n))
        res = [left+right]
        for i in range(1,n):
            delta = nums[i]-nums[i-1]
            left += delta*i 
            right -= delta*(n-i)
            res.append(left+right)
        return res 