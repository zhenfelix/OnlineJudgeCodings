class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        mp = defaultdict(int)
        n = len(s)
        for i in range(n):
            delta = (ord(t[i])-ord(s[i]))%26
            # print(delta)
            nxt = mp[delta]
            if nxt > 0:
                mp[delta] += 26
            else:
                mp[delta] = delta
            if mp[delta] > k:
                return False
        return True