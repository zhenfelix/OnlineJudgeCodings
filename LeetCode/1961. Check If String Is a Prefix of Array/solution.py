class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        n = len(words)
        return any(s == ''.join(words[:i+1]) for i in range(n))