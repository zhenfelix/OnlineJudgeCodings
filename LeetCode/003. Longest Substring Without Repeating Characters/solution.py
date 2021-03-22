from __future__ import annotations


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        dp = 0
        mp = {}
        for i, ch in enumerate(s):
            if ch in mp and mp[ch]+dp>=i:
                dp = i-mp[ch]
            else:
                dp += 1
            mp[ch] = i
            ans = max(ans, dp)
        return ans

s = Solution()
sr = "abcabcbb"

s.lengthOfLongestSubstring(sr)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp, res, n = 0, 0, len(s)
        last = [-1]*256
        for i in range(n):
            dp = max(dp, last[ord(s[i])]+1)
            res = max(res, i-dp+1)
            last[ord(s[i])] = i
        return res