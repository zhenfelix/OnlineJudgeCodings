class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        if not pattern:
            return not value
        if pattern[0] == 'b':
            pattern = ''.join(['a' if ch == 'b' else 'b' for ch in pattern])
        cnta, cntb = pattern.count('a'), pattern.count('b')
        if cntb: idxb = pattern.index('b')
        maxsza = len(value)//cnta
        for sza in range(maxsza+1):
            szb = len(value)-sza*cnta
            if (cntb == 0 and szb != 0) or (cntb != 0 and szb%cntb): continue
            if cntb: szb //= cntb
            if (cnta == cntb == 0) or (cntb and value[:sza] == value[idxb*sza:idxb*sza+szb]): continue
            candidate = ''.join([value[:sza] if ch == 'a' else value[idxb*sza:idxb*sza+szb] for ch in pattern])
            if candidate == value:
                return True
        return False
