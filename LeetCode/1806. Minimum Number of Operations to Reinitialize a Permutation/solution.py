# class Solution:
#     def reinitializePermutation(self, n):
#         res, i = 0, 1
#         while res == 0 or i > 1:
#             i = i * 2 % (n - 1)
#             res += 1
#         return res        

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        p = [i//2 if i%2 == 0 else n//2+(i-1)//2 for i in range(n)]
        parent = [i for i in range(n)]
        # print(p)
        def find(cur):
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
            return
        for i in range(n):
            union(i,p[i])
        # print([find(i) for i in parent])
        cc = Counter([find(i) for i in parent])
        cc = set(cc.values())
        # print(cc)
        if len(cc) == 1:
            return cc.pop()
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        return reduce(lambda a,b: a*b//gcd(a,b), cc)