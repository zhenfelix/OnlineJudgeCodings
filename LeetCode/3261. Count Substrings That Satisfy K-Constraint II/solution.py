class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        cnt = l = 0
        n = len(s)
        left = [0]*n
        ps = [0]*(n+1)  
        for r in range(n):
            cnt += int(s[r])
            while (cnt > k) and (r-l+1-cnt > k):
                cnt -= int(s[l])
                l += 1
            # print(cnt)
            left[r] = l 
        for i in range(n):
            ps[i] += ps[i-1]+(i-left[i]+1)
        ans = []
        # print(left,ps)
        for i, j in queries:
            lo, hi = i, j  
            while lo <= hi:
                m = (lo+hi)//2
                if left[m] > i:
                    hi = m-1
                else:
                    lo = m+1
            tmp = 0
            if lo > i: tmp += (lo-i)*(lo-i+1)//2
            if lo <= j: tmp += ps[j]-ps[lo-1]
            ans.append(tmp)
        return ans 
