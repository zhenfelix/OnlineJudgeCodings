class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        lo, hi = [0]*n, [0]*n 
        for i in range(1,n):
            if security[i] <= security[i-1]:
                lo[i] = lo[i-1]+1
        for i in range(n-1)[::-1]:
            if security[i] <= security[i+1]:
                hi[i] = hi[i+1]+1
        res = []
        for i in range(n):
            if lo[i] >= time and hi[i] >= time:
                res.append(i)
        return res