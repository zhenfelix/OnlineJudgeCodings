class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        n = len(nums)
        ans = [-1]*n
        def dfs(cur,parent,depth,mp):
            res = (-1, -1)
            for k, v in mp.items():
                if v and gcd(k,nums[cur]) == 1:
                    res = max(res,v[-1])
            ans[cur] = res[-1]
            mp[nums[cur]].append((depth,cur))
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                dfs(nxt,cur,depth+1,mp)
            mp[nums[cur]].pop()
            return
        mp_ = defaultdict(list)
        dfs(0,-1,0,mp_)
        return ans 

