# class Solution:
#     def mergeStones(self, stones: List[int], K: int) -> int:
#         n = len(stones)
#         if K != 2 and n%(K-1) != 1:
#             return -1
#         rounds = n//(K-1)
#         res = 0
#         while len(stones) > 1:
#             print(stones)
#             sums = sum(stones[:K])
#             idx, target = 0, sums
#             for i in range(K,len(stones)):
#                 sums = sums + stones[i] - stones[i-K]
#                 if sums < target:
#                     idx = i-K+1
#                     target = sums
#             stones = stones[:idx] + [target] + stones[idx+K:]
#             res += target
#         return res
            


# class Solution:
#     def mergeStones(self, stones: List[int], K: int) -> int:
#         n = len(stones)
#         if K != 2 and n%(K-1) != 1:
#             return -1
#         prefix = [0]*(n+1)
#         for i in range(n):
#             prefix[i+1] = prefix[i] + stones[i]
#         def dfs(left,right,m):
#             if (left,right,m) in memo:
#                 return memo[left,right,m]
#             if left == right:
#                 memo[left,right,m] = (0 if m == 1 else float('inf'))
#                 return memo[left,right,m]
#             if m == 1:
#                 # memo[left,right,m] = sum(stones[left:right+1]) + dfs(left,right,K)
#                 memo[left,right,m] = dfs(left,right,K) + prefix[right+1]-prefix[left]
#             else:
#                 memo[left,right,m] = min([dfs(left,k,1)+dfs(k+1,right,m-1) for k in range(left,right,K-1)])
#             return memo[left,right,m]

#         memo = {}
#         dfs(0,len(stones)-1,1) 
#         # print(memo)
#         return memo[0,len(stones)-1,1]


#     def mergeStones(self, stones, K):
#         n = len(stones)
#         inf = float('inf')
#         prefix = [0] * (n + 1)
#         for i in range(n):
#             prefix[i + 1] = prefix[i] + stones[i]

#         import functools

#         @functools.lru_cache(None)
#         def dp(i, j, m):
#             if (j - i + 1 - m) % (K - 1):
#                 return inf
#             if i == j:
#                 return 0 if m == 1 else inf
#             if m == 1:
#                 return dp(i, j, K) + prefix[j + 1] - prefix[i]
#             return min(dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j, K - 1))
#         res = dp(0, n - 1, 1)
#         return res if res < inf else -1


class Solution:
#     def mergeStones(self, stones: List[int], K: int) -> int:
#         n = len(stones)
#         if K != 2 and n%(K-1) != 1:
#             return -1
#         prefix = [0]*(n+1)
#         for i in range(n):
#             prefix[i+1] = prefix[i] + stones[i]
#         def dfs(left,right):
#             if (left,right) in memo:
#                 return memo[left,right]
#             if left == right:
#                 memo[left,right] = 0
#                 return memo[left,right]
#             memo[left,right] = min([dfs(left,k)+dfs(k+1,right) for k in range(left,right,K-1)])
#             if (right-left)%(K-1) == 0:
#                 memo[left,right] += prefix[right+1]-prefix[left]
#             return memo[left,right]

#         memo = {}
#         dfs(0,len(stones)-1) 
#         # print(memo)
#         return memo[0,len(stones)-1]

    def mergeStones(self, stones, K):
        n = len(stones)
        if (n - 1) % (K - 1): return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools
        @functools.lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K: return 0
            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))
            if (j - i) % (K - 1) == 0:
                res += prefix[j + 1] - prefix[i]
            return res
        return dp(0, n - 1)

