class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        for ch in s:
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1
        for i, ch in enumerate(s):
            if mp[ch] == 1:
                return i
        return -1