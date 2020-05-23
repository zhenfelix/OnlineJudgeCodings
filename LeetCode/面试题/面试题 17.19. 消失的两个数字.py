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