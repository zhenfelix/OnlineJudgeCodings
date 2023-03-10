class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        tot = Counter(s)
        cc = Counter()
        pos = dict()
        ans = inf  
        n = len(s)
        for i, ch in enumerate(s+'z'):
            mx = 0 
            for c in 'abc':
                if tot[c] >= k: continue
                if (c,k-tot[c]) not in pos: 
                    mx = inf 
                    continue
                mx = max(mx, pos[c,k-tot[c]])
            ans = min(ans, n-i+mx)
            cc[ch] += 1
            pos[ch,cc[ch]] = i+1
            tot[ch] -= 1
        return -1 if ans == inf else ans 