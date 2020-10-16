class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        s = str(N)
        n = len(s)
        dp = [1]*n
        dp[0] = 0
        for i in range(2,n):
            dp[i] = dp[i-1]*(9-i+2)
        
        for i in range(1,n):
            dp[i] *= 9
            dp[i] += dp[i-1]
        # print(dp)
        

        def repeat(candidate):
            return len(set(candidate)) < len(candidate)

        def permute(x,y):
            sums = 1
            for _ in range(y):
                sums *= x
                x -= 1
            return sums

        
        def dfs(idx,prefix):
            if idx == n:
                return not repeat(prefix)
            cnt = 0
            start = 0 if idx else 1
            for ch in range(start,int(s[idx])):
                if repeat(prefix+str(ch)):
                    continue
                cnt += permute(9-idx,n-1-idx)
            # print(idx,prefix,cnt)
            cnt += dfs(idx+1,prefix+s[idx])
            
            return cnt
        return N-(dfs(0,'')+dp[n-1])
