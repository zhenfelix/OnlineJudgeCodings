class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n)[::-1]:
            if int(num[i])&1:
                return num[:i+1]
        return ""