class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        def transform(s):
            v = []
            for i, ch in enumerate(s):
                if ch != 'X':
                    v.append((ch,i))
            return v 
        v1, v2 = transform(start), transform(end)
        if len(v1) != len(v2):
            return False
        for (ch1,i), (ch2,j) in zip(v1,v2):
            if ch1 != ch2:
                return False
            if ch1 == 'L':
                if i < j:
                    return False
            else:
                if i > j:
                    return False
        return True

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