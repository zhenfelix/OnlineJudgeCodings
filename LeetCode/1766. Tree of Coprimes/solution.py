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

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        pp = defaultdict(list)
        pp[1].append(1)
        for v in range(1,51):
            for u in range(v+1,51):
                if gcd(v,u) == 1:
                    pp[v].append(u)
                    pp[u].append(v)
        ans = [-1]*n 
        depth = [-1]*n
        mp = [-1]*51
        def dfs(cur,parent,d):
            v = nums[cur]
            mx = -1
            for u in pp[v]:
                if mp[u] >= 0 and depth[mp[u]] > mx:
                    mx = depth[mp[u]]
                    ans[cur] = mp[u]
            depth[cur] = d
            pre = mp[v]
            mp[v] = cur 
            for nxt in g[cur]:
                if nxt == parent: continue
                dfs(nxt,cur,d+1)
            mp[v] = pre
            return  
        dfs(0,0,0)
        return ans 