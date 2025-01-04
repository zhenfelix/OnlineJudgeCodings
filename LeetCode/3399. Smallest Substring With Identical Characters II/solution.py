class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        def check(limit,arr):
            cnt = 1
            ops = 0
            for i in range(1,n):
                
                if arr[i] == arr[i-1]:
                    cnt += 1
                if arr[i] != arr[i-1] or i == n-1:
                    ops += cnt//(limit+1)
                    cnt = 1
                if ops > numOps:
                    return False
            return ops <= numOps
        def doit(flag,arr):
            cnt = 0
            for i in range(n):
                cnt += arr[i]==((i&1)^flag)
            return cnt

        s = list(map(int,s))
        if min(doit(0,s),doit(1,s)) <= numOps:
            return 1  

        lo, hi = 2, n 
        while lo <= hi:
            m = (lo+hi)//2
            if check(m,s):
                hi = m-1
            else:
                lo = m+1
        return lo
        return ans
