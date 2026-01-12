class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        from itertools import accumulate
        from bisect import bisect_left
        p = [0] + list(accumulate(damage))
        ans = 0
        for k, r in enumerate(requirement):
            ans += k + 1 - bisect_left(p, p[k+1] + r - hp, hi=k+1)
        return ans