class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur, res = 0, 0
        for g in gain:
            cur += g 
            res = max(res, cur)
        return re