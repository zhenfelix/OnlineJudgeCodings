class Solution:
    def minDeletions(self, s: str) -> int:
        cc = Counter(s)
        arr = sorted([cc[k] for k in cc], reverse=True)
        reach, res = float('inf'), 0
        for a in arr:
            if reach < a:
                res += a-reach
            reach = min(reach-1,a-1)
            reach = max(reach,0)
        return res 