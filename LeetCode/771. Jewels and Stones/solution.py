import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        mp = collections.Counter(S)
        print(mp)
        # Set = set(J)
        for ch in J:
            res += mp[ch]
        return res
        