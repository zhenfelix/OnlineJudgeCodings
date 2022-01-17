class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        res = []
        for i in range(0,n,k):
            cur = s[i:i+k]
            if len(cur) < k:
                cur = cur+(fill*(k-len(cur)))
            res.append(cur)
        return res