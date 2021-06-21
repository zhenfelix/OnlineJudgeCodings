class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sums = sum(chalk)
        k %= sums
        n = len(chalk)
        for i in range(n):
            if k < chalk[i]:
                return i 
            k -= chalk[i]
        return -1