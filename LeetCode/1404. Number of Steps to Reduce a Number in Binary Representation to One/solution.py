class Solution:
    def numSteps(self, s: str) -> int:
        carry, cnt = 0, 0
        for cur in s[1:][::-1]:
            cur = int(cur)
            cnt += (carry^cur)
            carry = (carry|cur)
        return cnt+len(s)-1+carry