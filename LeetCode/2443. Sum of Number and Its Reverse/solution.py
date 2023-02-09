
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def convert(x):
            y = 0
            while x:
                y = y*10+x%10
                x //= 10
            return y 
        for k in range(num+1):
            if k+convert(k) == num:
                return True 
        return False