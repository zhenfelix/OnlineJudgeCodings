# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         lo, hi = min(bloomDay), max(bloomDay)
#         def calc(x):
#             tot, res = 0, 0
#             for i, d in enumerate(bloomDay+[float('inf')]):
#                 if d <= x:
#                     tot += 1
#                 else:
#                     res += tot//k
#                     tot = 0
#             return res

#         while lo <= hi:
#             mid = (lo+hi)//2
#             cc = calc(mid)
#             # print(mid,cc)
#             if cc >= m:
#                 hi = mid-1
#             else:
#                 lo = mid+1
#         if lo > max(bloomDay):
#             return -1
#         else:
#             return lo


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        lo, hi = min(bloomDay), max(bloomDay)
        def calc(x):
            tot, res = 0, 0
            for i, d in enumerate(bloomDay+[float('inf')]):
                if d <= x:
                    tot += 1
                else:
                    res += tot//k
                    tot = 0
            return res

        while lo <= hi:
            mid = (lo+hi)//2
            cc = calc(mid)
            # print(mid,cc)
            if cc >= m:
                hi = mid-1
            else:
                lo = mid+1
        return lo


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        n = len(bloomDay)
        idx = sorted(range(n), key=lambda x: bloomDay[x])
        total = 0
        sz = Counter()
        parent = [i for i in range(n)]

        def find(cur):
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]

        def union(left,right):
            rl = find(left)
            rr = find(right)
            parent[rl] = rr
            sz[rr] += sz[rl]


        for i in idx:
            sz[i] = 1
            total += sz[find(i)]//k
            if sz[i-1]:
                total -= sz[find(i-1)]//k
                total -= sz[find(i)]//k
                union(i-1,i)
                total += sz[find(i)]//k
            if sz[i+1]:
                total -= sz[find(i)]//k
                total -= sz[find(i+1)]//k
                union(i,i+1)
                total += sz[find(i+1)]//k 
            if total >= m:
                return bloomDay[i]
        return -1
