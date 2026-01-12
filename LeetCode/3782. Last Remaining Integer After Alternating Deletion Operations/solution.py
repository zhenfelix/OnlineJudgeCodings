class Solution:
    def lastInteger(self, n: int) -> int:
        if n == 1:
            return 1
        m = (n + 1) // 2
        return 2 * (m + 1 - self.lastInteger(m)) - 1