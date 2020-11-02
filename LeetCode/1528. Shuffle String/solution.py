class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        # res = [None]*n
        # for i, ch in enumerate(s):
        #     res[indices[i]] = ch
        # return ''.join(res)
        s = list(s)
        for i in range(n):
            while indices[i] != i:
                nxt = indices[i]
                indices[i], indices[nxt] = indices[nxt], indices[i]
                s[i], s[nxt] = s[nxt], s[i]
        return ''.join(s)