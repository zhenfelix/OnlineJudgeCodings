class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9+7
        cnt = 0
        mx = -1
        for a, b in sorted(ranges):
            if a > mx:
                cnt += 1
            mx = max(mx,b)
        return pow(2,cnt,MOD)