class Solution:
    def longestWPI(self, hours):
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score not in seen:
                seen[score] = i
            if score > 0:
                res = i + 1
            elif score - 1 in seen:
                res = max(res, i - seen[score - 1])
            
        return res