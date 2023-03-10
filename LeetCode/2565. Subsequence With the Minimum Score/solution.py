class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(t), len(s)
        j = m-1
        st = []
        for i in range(n)[::-1]:
            while j >= 0 and s[j] != t[i]:
                j -= 1
            if j < 0: break
            st.append((i,j))
            j -= 1
            
        # print(st[::-1])
        j = 0
        ans = n if not st else st[-1][0]
        for i in range(n):
            while j < m and s[j] != t[i]:
                j += 1
            while st and (st[-1][0] <= i or st[-1][1] <= j):
                st.pop()
            j += 1
            if j > m: break
            sz = i+1
            if st:
                sz += n-st[-1][0]

            # print(i,j,sz,n-sz)
            ans = min(ans, n-sz)
        return ans 
        
