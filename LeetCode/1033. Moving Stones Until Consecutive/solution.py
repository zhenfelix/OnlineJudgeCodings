class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = abs(a-b), abs(b-c), abs(a-c)
        lo, hi = min(a,b,c), max(a,b,c)
        if hi == 2:
            return [0,0]
        return [1 if lo in [1,2] else 2, hi-2]