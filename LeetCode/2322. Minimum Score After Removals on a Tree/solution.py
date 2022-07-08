class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        tot = 0
        for a in nums:
            tot ^= a 
        # print(tot)
        ans = float('inf')
        dp = [0]*n 
        tin, tout = [-1]*n, [-1]*n 
        clock = 0

        def dfs(cur, parent):
            nonlocal clock
            clock += 1
            tin[cur] = clock
            sums = 0
            sums ^= nums[cur]
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                dfs(nxt, cur)
                sums ^= dp[nxt]
            dp[cur] = sums
            clock += 1
            tout[cur] = clock
            return

        def isAncestor(a, b):
            return tin[a] < tin[b] and tout[a] > tout[b]

        dfs(0,-1)
        for i in range(1,n):
            for j in range(i+1,n):
                if isAncestor(i,j):
                    x, y, z = dp[j], dp[i]^dp[j], tot^dp[i]
                elif isAncestor(j,i):
                    x, y, z = dp[i], dp[i]^dp[j], tot^dp[j]
                else:
                    x, y, z = dp[i], dp[j], tot^dp[i]^dp[j]
                mx, mi = max(x,y,z), min(x,y,z)
                ans = min(ans, mx-mi)
        return ans



class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        tot = 0
        for a in nums:
            tot ^= a 
        # print(tot)
        ans = float('inf')
        clock = 0
        dp = defaultdict(int)
        tin = [-1]*n 
        tout = [-1]*n 

        def dfs(cur, parent):
            nonlocal ans, clock
            clock += 1
            tin[cur] = clock
            sums = 0
            sums ^= nums[cur]
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                tsums = dfs(nxt, cur)
                sums ^= tsums
            clock += 1
            tout[cur] = clock
            if parent != -1:
                for a, b in edges:
                    if ((a,b) not in dp) and ((b,a) not in dp):
                        continue
                    if (b,a) in dp:
                        a, b = b, a 
                    tmp = dp[a,b]
                    if tin[cur] < tin[a] and tout[a] < tout[cur]:
                        x, y, z = sums^tmp, tmp, tot^sums
                    # elif tin[a] < tin[cur] and tout[a] == -1:
                    #     x, y, z = sums, sums^tmp, tot^tmp
                    else:
                        x, y, z = sums, tmp, tot^sums^tmp
                    mx = max(x, y, z)
                    mi = min(x, y, z)
                    ans = min(ans, mx-mi)
                    # if (mx-mi) == 6:
                    #     print(cur,parent, a,b)

            dp[cur,parent] = sums
            return sums

        dfs(0,-1)
        # print(dp)
        return ans
