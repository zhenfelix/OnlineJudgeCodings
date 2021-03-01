class Solution:
    def minOperations(self, s: str) -> int:
        res = [0, 0]
        for i, ch in enumerate(s):
            res[(i&1)^int(ch)] += 1
        return min(res)

    def minOperations(self, s):
        res = sum(i % 2 == int(c) for i, c in enumerate(s))
        return min(res, len(s) - res)