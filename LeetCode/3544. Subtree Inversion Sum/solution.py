class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        memo = {}
        def dfs(cur,pre,sign,dist):
            t = (cur,sign,dist)
            if t in memo:
                return memo[t]
            ans = -inf
            s = nums[cur] if sign == 1 else -nums[cur]
            for nxt in g[cur]:
                if nxt == pre: continue
                s += dfs(nxt,cur,sign,dist if dist >= k else dist+1)
            ans = max(ans, s) 
            if dist >= k:
                s = nums[cur] if sign == -1 else -nums[cur]
                for nxt in g[cur]:
                    if nxt == pre: continue
                    s += dfs(nxt,cur,-sign,1)
                ans = max(ans, s) 
            # print(cur,sign,dist,ans)
            memo[t] = ans
            return ans 
        return dfs(0,0,1,k)
