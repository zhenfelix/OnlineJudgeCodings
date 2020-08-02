class Solution:
    def numSub(self, s: str) -> int:
        res, cur = 0, 0
        for ch in s:
            if ch == '0':
                cur = 0
            else:
                cur += 1
                res += cur
        return res%(10**9+7)