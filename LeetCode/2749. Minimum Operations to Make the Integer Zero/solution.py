class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        ans = 0
        for _ in range(100):
            if num1 <= 0: break
            ans += 1
            num1 -= num2
            # if bin(num1)[2:].count('1') <= ans: break 
            if num1.bit_count() <= ans: break 
        if num1 >= ans: return ans 
        return -1