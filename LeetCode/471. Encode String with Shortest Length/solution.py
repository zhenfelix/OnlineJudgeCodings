class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        def compress(i,j):
            # print(i,j,s)
            # if i == j:
            #     return s[i]
            tmp = s[i:j+1]
            m = len(tmp)
            Next = [-1]*(m+1)
            ii, jj = 0, -1
            while ii < m:
                if jj == -1 or tmp[ii] == tmp[jj]:
                    ii += 1
                    jj += 1
                    Next[ii] = jj
                else:
                    jj = Next[jj]
            diff = m - Next[-1]
            # print(Next)
            # print(diff)
            if Next[-1] > 0 and m%diff == 0:
                pattern = str(m//diff)+'['+dp[i,i+diff-1]+']'
                if len(pattern) < m:
                    return pattern
            return s[i:j+1]
            
            
        dp = {}
        for k in range(n):
            i, j = 0, k
            while j < n:
                dp[i,j] = compress(i,j)
                for mid in range(i,j):
                    if len(dp[i,mid]+dp[mid+1,j]) <= len(dp[i,j]):
                        dp[i,j] = dp[i,mid]+dp[mid+1,j]
                i += 1
                j += 1
        return dp[0,n-1]