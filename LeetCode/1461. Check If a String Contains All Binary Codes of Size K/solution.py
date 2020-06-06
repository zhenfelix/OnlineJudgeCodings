class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        cur = 0
        ss = set()
        for i, ch in enumerate(s):
            if i-k >= 0 and s[i-k] == '1':
                cur -= (1<<(k-1))
            cur = cur<<1
            if ch == '1':
                cur += 1
            
            if i >= k-1:
                ss.add(cur)
        # print(ss)
        return len(ss) == (1<<k)