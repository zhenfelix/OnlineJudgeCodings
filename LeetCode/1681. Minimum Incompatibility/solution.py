class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        import itertools
        import collections
        import sys

        def search(d, sum):
            nonlocal res, m
            if sum >= res : return
            if d == k :
                res = sum
                return

            # a = sorted(itertools.filterfalse(lambda x:c[x]==0, c.keys()))
            a = sorted([x for x in c if c[x]])
            # a = [x for x in c if c[x]]
            if len(a) < m : return

            c[a[0]] -= 1
            for b in itertools.combinations(a[1:], m-1) :
                for i in b : c[i] -= 1
                search(d+1, sum+b[-1]-a[0])
                for i in b : c[i] += 1
            c[a[0]] += 1
                
        n = len(nums)
        if n == k : return 0

        c = Counter(nums)
        m, res = n // k, sys.maxsize
        search(0, 0)
        return res if res < sys.maxsize else -1


# class Solution:
#     def minimumIncompatibility(self, nums: List[int], k: int) -> int:
#         L = len(nums)
#         k = L // k
            
#         @lru_cache(None)
#         def f(av):
#             ns = []
#             for i in range(L):
#                 if av & (1 << i) == 0:
#                     ns.append(i)
#             if not ns:
#                 return 0
            
#             d = 1e9
#             for c in itertools.combinations(ns, k):
#                 iii = c
#                 c = [nums[i] for i in c]
#                 if len(set(c)) != len(c):
#                     continue
                
#                 m = av
#                 for n in iii:
#                     m |= (1 << n)
#                 dd = max(c) - min(c)
#                 dd = dd + f(m)
#                 d = min(d, dd)
#             # print(ns, d)
#             return d
        
#         r = f(0) 
#         return r if r < 1e8 else -1


# class Solution:
#     def minimumIncompatibility(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         # 特殊判断，如果元素数量等于组数
#         if n == k:
#             return 0
        
#         value = dict()
#         for sub in range(1 << n):
#             # 判断 sub 是否有 n/k 个 1
#             if bin(sub).count("1") == n // k:
#                 # 使用哈希表进行计数
#                 freq = set()
#                 flag = True
#                 for j in range(n):
#                     if sub & (1 << j):
#                         # 任意一个数不能出现超过 1 次
#                         if nums[j] in freq:
#                             flag = False
#                             break
#                         freq.add(nums[j])
                
#                 # 如果满足要求，那么计算 sub 的不兼容性
#                 if flag:
#                     value[sub] = max(freq) - min(freq)
        
#         f = dict()
#         f[0] = 0
#         for mask in range(1 << n):
#             # 判断 mask 是否有 n/k 倍数个 1
#             if bin(mask).count("1") % (n // k) == 0:
#                 # 枚举子集
#                 sub = mask
#                 while sub > 0:
#                     if sub in value and mask ^ sub in f:
#                         if mask not in f:
#                             f[mask] = f[mask ^ sub] + value[sub]
#                         else:
#                             f[mask] = min(f[mask], f[mask ^ sub] + value[sub])
#                     sub = (sub - 1) & mask
            
#         return -1 if (1 << n) - 1 not in f else f[(1 << n) - 1]

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        value = dict()
        for sub in range(1 << n):
            # 判断 sub 是否有 n/k 个 1
            if bin(sub).count("1") == n // k:
                # 使用哈希表进行计数
                freq = set()
                flag = True
                for j in range(n):
                    if sub & (1 << j):
                        # 任意一个数不能出现超过 1 次
                        if nums[j] in freq:
                            flag = False
                            break
                        freq.add(nums[j])
                
                # 如果满足要求，那么计算 sub 的不兼容性
                if flag:
                    value[sub] = max(freq) - min(freq)
        
        f = dict()
        f[0] = 0
        for mask in range(1 << n):
            # 判断 mask 是否有 n/k 倍数个 1
            if bin(mask).count("1") % (n // k) == 0:
                # 如果子集个数小于 value 中满足要求的子集个数，我们才枚举子集
                if 2**bin(mask).count("1") < len(value):
                    sub = mask
                    while sub > 0:
                        if sub in value and mask ^ sub in f:
                            if mask not in f:
                                f[mask] = f[mask ^ sub] + value[sub]
                            else:
                                f[mask] = min(f[mask], f[mask ^ sub] + value[sub])
                        sub = (sub - 1) & mask
                else:
                    for sub, v in value.items():
                        if (mask & sub) == sub and mask ^ sub in f:
                            if mask not in f:
                                f[mask] = f[mask ^ sub] + v
                            else:
                                f[mask] = min(f[mask], f[mask ^ sub] + v)
            
        return -1 if (1 << n) - 1 not in f else f[(1 << n) - 1]




# class Solution:
#     def minimumIncompatibility(self, nums: List[int], k: int) -> int:
#         self.kn = len(nums) // k
#         nums = sorted(nums)

#         @functools.lru_cache(None)
#         def solve(state = 0, lastp = -1) :
#             p0s = [i for i in range(len(nums)) if not (1<<i) & state]
#             if len(p0s) == 0 :
#                 return 0

#             if len(p0s) % self.kn == 0 :
#                 return solve(state|(1<<p0s[0]), p0s[0])
            
#             # # 一个有意思的剪枝
#             # if len(p0s) % self.kn > 1 :
#             #     p0s = p0s[:- (len(p0s) % self.kn -  1)]
            
#             to_ret = 1e99
#             for t in p0s :
#                 if nums[t] <= nums[lastp] :
#                     continue

#                 to_ret = min(to_ret, nums[t] - nums[lastp] + solve(state|(1<<t), t))
#             return to_ret
            
#         to_ret = solve()
#         if to_ret > 1e66 :
#             return -1
#         return to_ret

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        self.kn = len(nums) // k
        if self.kn == 1:
            return 0
        nums = sorted(nums)
        n = len(nums)
        # print(nums)

        @functools.lru_cache(None)
        def solve(state = (1<<n)-1, lastp = -1) :
            p0s = [i for i in range(len(nums)) if (1<<i) & state]
            if state == 0 :
                return 0

            if len(p0s) % self.kn == 0 :
                return solve(state^(1<<p0s[0]), p0s[0])
            
            
            to_ret = 1e99
            for cur in p0s:
                if nums[cur] > nums[lastp]:
                    to_ret = min(to_ret, nums[cur] - nums[lastp] + solve(state^(1<<cur), cur))
            # print(state,lastp,to_ret)
            return to_ret
            
        to_ret = solve()
        if to_ret > 1e66 :
            return -1
        return to_ret