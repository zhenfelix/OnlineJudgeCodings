# from functools import lru_cache
# from math import sqrt
# class Solution:
#     def numFactoredBinaryTrees(self, A: List[int]) -> int:
#         cc = set(A)
#         @lru_cache(None)
#         def dfs(root):
#             if root not in cc:
#                 return 0
#             res = 1
#             i = 2
#             while i*i <= root:
#                 if root%i == 0:
#                     j = root//i 
#                     res += dfs(i)*dfs(j)*(2 if i!=j else 1)
#                 i += 1
#             return res
#         return sum(dfs(a) for a in A)%(10 ** 9 + 7)


# from functools import lru_cache
# class Solution:
#     def numFactoredBinaryTrees(self, A: List[int]) -> int:
#         cc = set(A)
#         memo = {}
#         @lru_cache(None)
#         def dfs(root):
#             if root in memo:
#                 return memo[root]
#             if root not in cc:
#                 return 0
#             res = 1
#             i = 2
#             while i*i <= root:
#                 if root%i == 0:
#                     j = root//i 
#                     res += dfs(i)*dfs(j)*(2 if i!=j else 1)
#                 i += 1
#             memo[root] = res
#             return res
#         return sum(dfs(a) for a in A)%(10 ** 9 + 7)


class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        memo = collections.defaultdict(int)
        res = 0
        # A = sorted(A)
        A.sort()
        # for i, a in enumerate(sorted(A)):
        for i, a in enumerate(A):
            memo[A[i]] = 1
            j = 0
            while j < i and A[j]*A[j] <= A[i]:
                if A[i]%A[j] == 0:
                    memo[A[i]] += memo[A[j]]*memo[A[i]//A[j]]*(2 if A[j]!=A[i]//A[j] else 1)
                j += 1
            res += memo[A[i]]
            # print(A[i], memo[A[i]])
        
        return res%(10 ** 9 + 7)


    
# class Solution:
#     def numFactoredBinaryTrees(self, A):
#         dp = {}
#         for a in sorted(A):
#             dp[a] = sum(dp[b] * dp.get(a / b, 0) for b in dp if a % b == 0) + 1
#         return sum(dp.values()) % (10**9 + 7)