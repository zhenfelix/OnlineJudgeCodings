class Solution:
    def robotWithString(self, s: str) -> str:
        res, st = [], []
        n = len(s)
        arr = []
        for i, ch in enumerate(s):
            arr.append((ch,i))
        cur = 0
        for ch, i in sorted(arr):
            if i >= cur:
                while st and st[-1] <= ch:
                    res.append(st.pop())
                while cur <= i:
                    st.append(s[cur])
                    cur += 1
                # res.append(st.pop())              
        while st:
            res.append(st.pop())
        return ''.join(res)

class Solution:
    def robotWithString(self, s: str) -> str:
        res, st = [], []
        n = len(s)
        mp = defaultdict(list)
        for i, ch in enumerate(s):
            mp[ch].append(i)
        cur = 0
        for ch in range(26):
            ch = chr(ord('a')+ch)
            for i in mp[ch]:
                if i >= cur:
                    while st and st[-1] <= ch:
                        res.append(st.pop())
                    while cur <= i:
                        st.append(s[cur])
                        cur += 1
                    res.append(st.pop())
        while st:
            res.append(st.pop())
        return ''.join(res)