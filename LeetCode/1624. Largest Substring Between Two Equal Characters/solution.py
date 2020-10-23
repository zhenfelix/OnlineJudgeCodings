class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mp = {}
        res = -1
        for i, ch in enumerate(s):
            if ch not in mp:
                mp[ch] = i 
            else:
                res = max(res, i-mp[ch]-1)
        return res