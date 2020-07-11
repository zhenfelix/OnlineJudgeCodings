class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        mi, mx = float('inf'), -float('inf')
        seen, n = set(), len(arr)
        for a in arr:
            seen.add(a)
            if a > mx: mx = a 
            if a < mi: mi = a 
        if (mx-mi)%(n-1): return False
        delta = (mx-mi)//(n-1)
        if delta == 0: return True
        cur = mi 
        while cur < mx:
            cur += delta
            if cur not in seen: return False
        return True
