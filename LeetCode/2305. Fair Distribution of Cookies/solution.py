class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        n = len(cookies)
        cookies.sort(reverse = True)

        def dfs(idx, path, cur):
            nonlocal ans
            if cur > ans:
                return
            if idx == n:
                ans = cur
                # print(path)
                return 
            for i in range(k):
                path[i] += cookies[idx]
                dfs(idx+1, path, max(cur,path[i]))
                path[i] -= cookies[idx]
                # 对称性剪枝
                if path[i] == 0:
                    break
            return

        dfs(0, [0]*k, 0)
        return ans 


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        dp = [float('inf')]*(1<<n)
        dp[0] = 0
        mp = defaultdict(int)
        for i in range(n):
            mp[1<<i] = cookies[i]
        cost = [0]*(1<<n)
        for s in range(1,1<<n):
            cost[s] = cost[s-(s&-s)] + mp[s&-s]
        for _ in range(k):
            ndp = dp.copy()
            for mask in range(1,1<<n):
                cur = mask
                while cur:
                    ndp[mask] = min(ndp[mask], max(dp[mask-cur], cost[cur]))
                    cur = (cur-1)&mask
            dp = ndp

        return dp[-1] 