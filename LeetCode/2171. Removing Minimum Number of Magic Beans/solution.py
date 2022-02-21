class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        cc = Counter(beans)
        tot = sum(beans)
        res = float('inf')
        for i in range(n):
            res = min(res, tot-beans[i]*(n-i))
        return res
        