class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        @lru_cache(None)
        def dfs(cur,pre,out):
            delta = -inf
            s = xor = 0
            for nxt in g[cur]:
                if nxt == pre: continue
                a, b = dfs(nxt,cur,1), dfs(nxt,cur,0)
                if a > b:
                    s += a
                    xor ^= 1 
                    delta = max(delta, b-a)
                else:
                    s += b
                    delta = max(delta, a-b)
            xor ^= out  
            tmp = nums[cur]
            if xor:
                tmp ^= k  
            ans = max(s+tmp,s+delta+(tmp^k))
            # print(cur,pre,out,ans)
            return ans  
        return dfs(0,0,0)


