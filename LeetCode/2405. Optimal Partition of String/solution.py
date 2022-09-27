class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        cnt = 1
        for ch in s:
            if ch in seen:
                cnt += 1
                seen = set()
            seen.add(ch)
        return cnt