class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cc = Counter(s)
        res = []
        for ch in range(26)[::-1]:
            nxt = ord('a')+ch-1
            ch = chr(ord('a')+ch)
            if cc[ch] <= 0:
                continue
            while cc[ch] > 0:
                delta = min(cc[ch], repeatLimit)
                cc[ch] -= delta
                for _ in range(delta):
                    res.append(ch)
                if cc[ch] > 0:
                    while cc[chr(nxt)] <= 0 and chr(nxt) >= 'a':
                        nxt -= 1
                    if cc[chr(nxt)] <= 0:
                        break
                    cc[chr(nxt)] -= 1
                    res.append(chr(nxt))
        return ''.join(res)
