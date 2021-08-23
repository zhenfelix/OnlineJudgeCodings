class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x, y = min(nums), max(nums)
        def gcd(a,b):
            if b == 0:
                return a 
            return gcd(b, a%b)
        return gcd(x,y)

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x, y = min(nums), max(nums)
        while y:
            x, y = y, x%y
        return x