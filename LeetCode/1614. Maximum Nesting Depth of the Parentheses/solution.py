class Solution:
    def maxDepth(self, s: str) -> int:
        res, cur = 0, 0
        for ch in s:
            if ch == '(':
                cur += 1
                res = max(res, cur)
            elif ch == ')':
                cur -= 1
        return res
