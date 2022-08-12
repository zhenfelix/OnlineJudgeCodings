class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0]*26
        for i in range(n)[::-1]:
            ndp = [0]*26
            ch = ord(s[i])-ord('a')
            for j in range(26):
                ndp[j] = dp[j]
                if abs(j-ch) <= k:
                    ndp[j] = max(ndp[j], 1+dp[ch])
            dp = ndp
        return max(dp)