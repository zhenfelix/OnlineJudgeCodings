class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        g = defaultdict(list)
        for i, v in enumerate(nums):
            g[v].append(i)
        mx = max(nums)
        n = len(nums)
        m = n+mx-1
        parent = list(range(m))
        def find(cur):
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]
        def connect(u,v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
            return

        for f in range(2,mx+1):
            for v in range(f,mx+1,f):
                for u in g[v]:
                    connect(f-2+n,u)
        return len(set([find(i) for i in range(n)])) == 1




prime_dict = defaultdict(list)
flag = [True] * (10**5+1)
for i in range(2, 10**5+1):
    if flag[i]:
        prime_dict[i].append(i)
        x = i * 2
        while x <= 10**5:
            prime_dict[x].append(i)
            flag[x] = False
            x += i
prime_dict[1] = [1]
        

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        assert 1 <= len(nums) <= 10**5
        for i in nums:
            assert 1 <= i <= 10**5
        if len(nums)==1:
            return True
        if 1 in nums:
            return False
        fa = {x:x for x in nums}
        
        def get_fa(x):
            if x not in fa:
                fa[x] = x
                return x
            if fa[x] == x:
                return x
            fa[x] = get_fa(fa[x])
            return fa[x]
        
        
        for a in nums:
            a_fa = get_fa(a)
            for b in prime_dict[a]:
                b_fa = get_fa(b)
                if a_fa != b_fa:
                    fa[b_fa] = a_fa 
        
        res = set()
        for i in nums:
            tmp = get_fa(i)
            res.add(tmp)
        return len(res)==1
                
            
        
        
            
