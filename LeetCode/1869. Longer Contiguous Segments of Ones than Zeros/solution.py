class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones, zeros, cur = 0, 0, 0
        n = len(s)
        for i in range(n):
            if i and s[i] == s[i-1]:
                cur += 1
            else:
                cur = 1
            if s[i] == '1':
                ones = max(ones, cur)
            else:
                zeros = max(zeros, cur)
        return ones > zeros