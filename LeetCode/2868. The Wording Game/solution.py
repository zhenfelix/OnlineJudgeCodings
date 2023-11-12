class Solution:
    def canAliceWin(self, a: List[str], b: List[str]) -> bool:
        n, m = len(a), len(b)
        a.sort()
        b.sort()
        la, ra = [0]*n, [0]*n 
        l, r = 0, 0
        for i,s in enumerate(a):
            while l < m and b[l] <= s:
                l += 1
            la[i] = l 
            while r < m and b[r][0] <= chr(ord(s[0])+1):
                r += 1
            ra[i] = r 
        lb, rb = [0]*m, [0]*m  
        l, r = 0, 0 
        for i, s in enumerate(b):
            while l < n and a[l] <= s:
                l += 1
            lb[i] = l 
            while r < n and a[r][0] <= chr(ord(s[0])+1):
                r += 1
            rb[i] = r 

        @lru_cache(None)
        def dfs(i,flag):
            # print(i,flag)
            if flag == 0:
                if i >= n: return 0
                l, r = la[i], ra[i]
            else:
                if i >= m: return 0
                l, r = lb[i], rb[i]
            return ((dfs(l,flag^1)-dfs(r,flag^1)) == 0)+dfs(i+1,flag)
        return (dfs(0,0)-dfs(1,0)) == 1