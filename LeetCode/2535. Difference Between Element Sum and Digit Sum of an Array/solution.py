class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a, b = 0, 0
        for x in nums:
            a += x  
            while x:
                b += (x%10)
                x //= 10
        return abs(a-b)