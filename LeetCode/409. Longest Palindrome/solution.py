class Solution:
    def longestPalindrome(self, s: str) -> int:
        cc = Counter(s)
        return sum(v//2*2 for k,v in cc.items())  + any(v&1 for k,v in cc.items())