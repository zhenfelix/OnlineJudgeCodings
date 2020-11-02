class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        s = [(i,ch) for i,ch in enumerate(start) if ch != 'X']
        e = [(i,ch) for i,ch in enumerate(end) if ch != 'X']
        if len(s) !=  len(e):
            return False
        for (i,c1),(j,c2) in zip(s,e):
            if c1 != c2:
                return False
            if c1 == 'L':
                if i <  j:
                    return False
            else:
                if i > j:
                    return False
        return True