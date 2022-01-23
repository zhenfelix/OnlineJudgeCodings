class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        cur, mi, mx = 0, 0, 0
        for d in differences:
            cur += d 
            mi = min(mi, cur)
            mx = max(mx, cur)
        return max(0, (upper-lower)-(mx-mi)+1)