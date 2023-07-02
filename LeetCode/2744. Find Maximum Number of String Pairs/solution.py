class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        ans = 0
        for s in words:
            if s in seen:
                ans += 1
            seen.add(s[::-1])
        return ans 
