class Solution:
    def brilliantSurprise(self, present: List[List[int]], limit: int) -> int:
        dp = [0]*(limit+1)
        ans = 0

        def calc(a, total):
            # nonlocal dp
            for s, b in zip(total,a):
                w = len(b)
                for cur in range(limit-w,-1,-1):
                    dp[cur+w] = max(dp[cur+w], dp[cur]+s)
            return

        def dfs(a, total):
            nonlocal ans, dp
            if len(a) == 1:
                s = 0
                for i, v in enumerate(a[0]):
                    if i == limit:
                        break
                    s += v 
                    ans = max(ans, s+dp[limit-i-1])
                    
                return 
            tmp = dp.copy()
            m = len(a)//2
            calc(a[m:],total[m:])
            dfs(a[:m],total[:m])

            dp = tmp
            calc(a[:m],total[:m])
            dfs(a[m:],total[m:])
            return

        tot = [sum(b) for b in present]
        dfs(present, tot)
        return ans 