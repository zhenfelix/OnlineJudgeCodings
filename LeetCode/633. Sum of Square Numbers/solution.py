class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        seen = set()
        i = 0
        while i*i <= c:
            seen.add(i*i)
            if c-i*i in seen:
                return True
            i += 1
        return False