class Solution:
    def minimizeXor(self, x: int, num2: int) -> int:
        n = str(bin(num2)).count('1')
        ans = 0
        for i in range(32)[::-1]:
            if n and (x>>i)&1:
                ans |= (1<<i)
                n -= 1
        for i in range(32):
            if n and ((x>>i)&1) == 0:
                ans |= (1<<i)
                n -= 1
        return ans 