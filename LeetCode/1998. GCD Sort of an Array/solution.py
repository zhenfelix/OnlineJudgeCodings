primes = []
# maxn = 10**5+5
# mask = [True]*maxn
# for i in range(2,maxn):
#     if mask[i]:
#         primes.append(i)
#         for j in range(i*i, maxn, i):
#             mask[j] = False
# print(primes)

maxn = 10**5+5
spf = [i for i in range(maxn)]
for i in range(2,maxn):
    if spf[i] == i:
        primes.append(i)
        for j in range(i*i, maxn, i):
            spf[j] = i


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        parent = {p:p for p in primes}
        mp = dict()
        def find(cur):
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]

        def connect(u, v):
            ru, rv = find(u), find(v)
            # print(ru,rv,u,v,"connecting")
            if ru != rv:
                parent[ru] = rv
            # print(find(u), find(v),"connected")
            return

        # def factor(x):
        #     fs = []
        #     f = 2
        #     for f in primes:
        #         if f > x:
        #             break
        #         if x%f == 0:
        #             fs.append(f)
        #         while x%f == 0:
        #             x //= f 
        #     return fs  

        # def factor(x):
        #     fs = []
        #     for f in primes:
        #         if f*f > x:
        #             break
        #         if x%f == 0:
        #             fs.append(f)
        #         while x%f == 0:
        #             x //= f 
        #     if x > 1:
        #         fs.append(x)
        #     return fs  

        def factor(x):
            fs = []
            while x > 1:
                if not fs or fs[-1] != spf[x]:
                    fs.append(spf[x])
                x //= spf[x]
            return fs  

        def merge(x):
            if x in mp:
                return
            fs = factor(x)
            # print(x,fs)
            if len(fs) > 1:
                for u, v in zip(fs,fs[1:]):
                    connect(u,v)
            # mp[x] = find(fs[0])
            mp[x] = fs[0]
            # print(x,mp[x])
            return

        for x in nums:
            merge(x)
        # print(mp)
        for x, y in zip(nums,sorted(nums)):
            if find(mp[x]) != find(mp[y]):
                # print(x, y, mp[x], mp[y])
                return False
        return True
