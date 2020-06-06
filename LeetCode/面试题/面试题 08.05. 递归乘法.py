class Solution:
    def multiply(self, a: int, b: int) -> int:
        if a > b:
            a, b = b, a
        if a == 0:
            return 0
        if a == 1:
            return b
        res = self.multiply(a>>1, b)
        return res + res + self.multiply(a&1, b)