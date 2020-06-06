class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        target = set(['a','e','i','o','u'])
        cnt, res = 0, 0
        for i, ch in enumerate(s):
            if ch in target: cnt += 1
            if i >= k and s[i-k] in target: cnt -= 1
            if i >= k-1: res = max(res,cnt)
        return res