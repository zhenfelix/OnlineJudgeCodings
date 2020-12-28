class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        left, right = 0, 0
        for i, ch in enumerate(s):
            if ch in "aeiouAEIOU":
                if i < n//2:
                    left += 1
                else:
                    right += 1
        return left == right