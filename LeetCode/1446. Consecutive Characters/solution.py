class Solution:
    def maxPower(self, s: str) -> int:
        res, pre = 0, ''
        cnt = 0
        for ch in s+' ':
            if ch != pre:
                res = max(res,cnt)
                cnt = 1
                pre = ch
            else:
                cnt += 1
        return res