class Solution:
    def minSwaps(self, s: str) -> int:
        n, ones, zeros, pos_one, pos_zero = len(s), 0, 0, 0, 0
        for i, ch in enumerate(s):
            if ch == "1":
                ones += 1
                if i&1:
                    pos_one += 1
            else:
                zeros += 1
                if not (i&1):
                    pos_zero += 1
        res = float("inf")
        if pos_one == pos_zero:
            res = min(res, pos_zero)
        if ones - pos_one == zeros - pos_zero:
            res = min(res, zeros- pos_zero)
        return -1 if res == float("inf") else res
