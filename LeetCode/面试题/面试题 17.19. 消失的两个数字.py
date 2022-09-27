class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        nums.append(0)
        nums.append(0)
        n = len(nums)
        for cur in range(1,n+1):
            pre = 0
            while cur and nums[cur-1] != cur:
                pre, nums[cur-1] = nums[cur-1], pre
                cur = pre
        ans = []
        for cur in range(1,n+1):
            if nums[cur-1] != cur:
                ans.append(cur)
        return ans

class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        z, n = 0, len(nums)+2
        for num in nums: z ^= num
        for i in range(1,n+1): z ^= i 
        z = z & (-z)
        a, b = 0, 0
        for num in nums:
            if num & z:
                a ^= num
            else:
                b ^= num
        for i in range(1,n+1):
            if i & z:
                a ^= i 
            else:
                b ^= i
        return [a,b]