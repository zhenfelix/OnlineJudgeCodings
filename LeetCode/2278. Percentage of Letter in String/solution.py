class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        ans = s.count(letter)/len(s)
        return int(ans*100)