class Solution:
    def reformat(self, s: str) -> str:
        ds, cs = [], []
        for ch in s:
            if '0' <= ch <= "9":
                ds.append(ch)
            else:
                cs.append(ch)
        if abs(len(ds)-len(cs)) > 1:
            return ""
        if len(ds) < len(cs):
            ds, cs = cs, ds
        res = []
        while ds:
            res.append(ds.pop())
            if cs:
                res.append(cs.pop())
        return ''.join(res)