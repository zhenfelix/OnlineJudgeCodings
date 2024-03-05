class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        mp = defaultdict(int)
        mx = 0
        for ch in s:
            mp[ch] += 1
            mx = max(mx,mp[ch])
        ans = []
        mp = defaultdict(int)
        for ch in s:
            mp[ch] += 1
            if mp[ch] == mx:
                ans.append(ch)
        return ''.join(ans)