class Solution:
    # def longestDecomposition(self, text: str) -> int:
    #     n, i = len(text), 0
    #     while i < n//2:
    #         if text[:i+1] == text[n-1-i:]:
    #             return 2+self.longestDecomposition(text[i+1:n-1-i])
    #         i += 1
    #     if text == "":
    #         return 0
    #     return 1
    
    
    def longestDecomposition(self, S):
        res, l, r = 0, "", ""
        for i, j in zip(S, S[::-1]):
            l, r = l + i, j + r
            if l == r:
                res, l, r = res + 1, "", ""
        return res