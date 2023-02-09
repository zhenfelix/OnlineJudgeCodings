class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        cnt = Counter()
        def dfs(cur, parent):
            s = nums[cur]
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                s += dfs(nxt, cur)
            cnt[s] += 1
            return s 
        tot = dfs(0,0)
        for f in range(1,tot+1):
            if tot%f == 0:
                s = f 
                cc = 0
                while s <= tot:
                    cc += cnt[s]
                    s += f 
                if cc == tot//f:
                    return cc-1
        return -1
                    

class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        tot = sum(nums)
        candidates = []
        for f in range(1,tot+1):
            if f*f > tot:
                break
            if tot%f == 0:
                candidates.append(f)
                candidates.append(tot//f)
            f += 1
        candidates.sort()
        # print(candidates)
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        def dfs(cur, parent, s):
            v = nums[cur]
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                nv = dfs(nxt, cur, s)
                v += nv 
            return 0 if v == s else v 



        for f in candidates:
            if dfs(0,0,f) == 0:
                return tot//f-1
        return 0
