class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(w == s[:len(w)] for w in words)