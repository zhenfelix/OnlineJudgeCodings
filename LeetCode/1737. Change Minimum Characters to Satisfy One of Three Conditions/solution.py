class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        la, lb = len(a), len(b)
        ca, cb = Counter(a), Counter(b)
        pa, pb = 0, 0
        res = la + lb
        for i in range(26):
            ch = chr(ord('a')+i)
            pa += ca[ch]
            pb += cb[ch]
            if i == 25:
                res = min(res, la-ca[ch]+lb-cb[ch])
            else:
                res = min(res, la-ca[ch]+lb-cb[ch], la-pa+pb, lb-pb+pa)
        return res 