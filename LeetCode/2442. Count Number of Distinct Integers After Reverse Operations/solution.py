class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def convert(x):
            y = 0
            while x:
                y = y*10+x%10
                x //= 10
            return y 
        n = len(nums)
        for i in range(n):
            nums.append(convert(nums[i]))
        return len(set(nums))