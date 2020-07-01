# from functools import lru_cache
# class Solution:
#     def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], K: int) -> int:
#         def count_ones(x):
#             cc = 0
#             while x:
#                 cc += 1
#                 x &= (x-1)
#             return cc 

#         @lru_cache(None)
#         def dfs(cur):
#             if cur == (1<<n)-1:
#                 return 0
#             available = 0
#             for j in range(n):
#                 if (cur & pre[j]) == pre[j]:
#                     available |= (1<<j)
#             available &= (~cur)
#             nxt = available
#             res = float('inf')
#             while nxt:
#                 if bin(nxt).count("1") <= K:
#                 # if count_ones(nxt) <= K:
#                     res = min(res,dfs(cur|nxt)+1)
#                 nxt = (nxt-1) & available
#             return res

#         pre = [0]*n
#         for a, b in dependencies:
#             a -= 1
#             b -= 1
#             pre[b] |= (1<<a)

#         return dfs(0)


# from functools import lru_cache
# class Solution:
#     def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], K: int) -> int:
#         def count_ones(x):
#             cc = 0
#             while x:
#                 cc += 1
#                 x &= (x-1)
#             return cc 

#         pre = [0]*n
#         for a, b in dependencies:
#             a -= 1
#             b -= 1
#             pre[b] |= (1<<a)

#         dp = [n]*(1<<n)
#         dp[0] = 0
#         for cur in range(1<<n):
#             available = 0
#             for j in range(n):
#                 if (cur & pre[j]) == pre[j]:
#                     available |= (1<<j)
#             available &= (~cur)
#             nxt = available
#             while nxt:
#                 if bin(nxt).count("1") <= K:
#                 # if count_ones(nxt) <= K:
#                     dp[nxt|cur] = min(dp[nxt|cur],dp[cur]+1)
#                 nxt = (nxt-1) & available

#         return dp[-1]


class Solution:
    def minNumberOfSemesters(self, N, edges, K):
        reqs = [0] * N
        for u, v in edges:
            reqs[v - 1] |= 1 << (u - 1)

        # dp[mask] = num of semesters to do all these courses
        # want dp[(1 << N) - 1]
        dp = [N] * (1 << N)
        dp[0] = 0
        
        for mask in range(1 << N):
            avail = []
            for v in range(N):
                if mask & (1 << v) == 0 and mask & reqs[v] == reqs[v]:
                    avail.append(v)
            
            for choice in itertools.combinations(avail, min(K, len(avail))):
                mask2 = mask
                for u in choice:
                    mask2 |= 1 << u
                dp[mask2] = min(dp[mask2], 1 + dp[mask])
        
        return dp[-1]

class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        pre = [0]*n
        for a, b in dependencies:
            a -= 1
            b -= 1
            pre[b] |= (1<<a)
        @functools.lru_cache(None)
        def dfs(cur):
            if cur == (1<<n)-1:
                return 0
            avail = []
            for i in range(n):
                if (1<<i)&cur == 0 and cur&pre[i] == pre[i]:
                    avail.append(i)
            res = float('inf')
            for choice in itertools.combinations(avail, min(k,len(avail))):
                nxt = cur
                for u in choice:
                    nxt |= (1<<u)
                res = min(res,dfs(nxt)+1)
            return res 
        return dfs(0)



# class Solution:
#     def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
#         if k == 1:
#             return n
#         b2i = {1<<i:i for i in range(n)} # binary representation to index        
#         dep = [0] * n # binary representation of dependencies
#         for a,b in dependencies:
#             dep[b-1] |= 1<<(a-1)
#         todo = (1<<n)-1
#         @functools.lru_cache(1<<16)
#         def search(todo):
#             if not todo:
#                 return 0
#             avail = []
#             tmp = todo
#             while(tmp):
#                 lowbit = tmp & (-tmp)
#                 idx = b2i[lowbit]
#                 if dep[idx]&todo==0:
#                     avail.append(idx)
#                 tmp ^= lowbit
#             if len(avail) <= k:
#                 for i in avail:
#                     todo ^= 1 << i
#                 return 1 + search(todo)
#             else:
#                 ans = 1<<16
#                 for takes in itertools.combinations(avail, k):
#                     tmp = todo
#                     for i in takes:
#                         tmp ^= 1 << i
#                     ans = min(ans, 1+search(tmp))
#                 return ans
#         return search(todo)
