class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        n = len(words)
        cc = Counter()
        odw, odch = 0, 0
        for ws in words:
            if len(ws)&1: odw += 1
            for ch in ws:
                cc[ch] += 1
        for k, v in cc.items():
            if v&1: odch += 1 
        if odw < odch:
            r = odch-odw
            cnts = sorted([len(ws) for ws in words],reverse=True)
            for c in cnts:
                if c&1: c -= 1
                if r > 0 and c > 0:
                    r -= c  
                    n -= 1
        return n 


