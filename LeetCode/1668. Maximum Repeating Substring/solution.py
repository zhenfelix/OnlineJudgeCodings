class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res, k = 0, 1
        while True:
            if word*k not in sequence:
                break
            res = k
            k += 1
        return res 