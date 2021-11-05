class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        return X - Y if X >= Y else 1 + Y % 2 + self.brokenCalc(X, (Y + 1) // 2)

class Solution:
    @lru_cache(None)
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue >= target:
            return startValue-target
        if target%2 == 0:
            return 1+self.brokenCalc(startValue, target//2)
        return 1+self.brokenCalc(startValue, target+1)