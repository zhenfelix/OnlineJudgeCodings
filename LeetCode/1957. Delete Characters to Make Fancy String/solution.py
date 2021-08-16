class Solution:
    def makeFancyString(self, s: str) -> str:
        res = [s[0]]
        cnt = 1
        for a, b in zip(s, s[1:]):
            if a == b and cnt == 2:
                continue
            if a == b:
                cnt += 1
            else:
                cnt = 1
            res.append(b)
        return ''.join(res)