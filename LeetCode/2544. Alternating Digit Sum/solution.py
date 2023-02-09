class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        flag = 1
        for ch in str(n):
            ans += flag*int(ch)
            flag = -flag
        return ans
