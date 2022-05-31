class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        b, e = s.split(':')
        lo, hi = int(b[1:]), int(e[1:])
        left, right = b[0], e[0]
        res = []
        for c in range(ord(left), ord(right)+1):
            for r in range(lo, hi+1):
                res.append(chr(c)+str(r))
        return res