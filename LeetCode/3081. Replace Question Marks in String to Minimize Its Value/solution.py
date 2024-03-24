class Solution:
    def minimizeStringValue(self, s: str) -> str:
        cc = Counter(s)
        ans = []
        candidates = []
        pos = []
        for i, ch in enumerate(s):
            if ch != '?':
                ans.append(ch)
            else:
                ans.append('a')
                for c in range(26):
                    c = chr(ord('a')+c)
                    if cc[c] < cc[ans[-1]]:
                        ans[-1] = c  
                cc[ans[-1]] += 1
                candidates.append(ans[-1])
                pos.append(i)
        candidates.sort()
        # print(candidates)
        for ch, i in zip(candidates,pos):
            ans[i] = ch 
        return ''.join(ans)