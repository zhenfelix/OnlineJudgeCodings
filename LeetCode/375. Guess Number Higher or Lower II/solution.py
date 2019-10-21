# class Solution:
#     def getMoneyAmount(self, n: int) -> int:
#         def dfs(left,right):
#             if (left,right) in memo:
#                 return memo[left,right]
#             if left >= right:
#                 memo[left,right] = 0
#                 return 0
#             pay = float('inf')
#             for choose in range(left,right+1):
#                 pay = min(pay, choose+max(dfs(left,choose-1), dfs(choose+1,right)))
#             memo[left,right] = pay
#             return pay
#         memo = {}
#         dfs(1,n)
#         print(memo)
#         return memo[1,n]


# import functools
# class Solution:
#     @functools.lru_cache(None)
#     def solve(self, l, r):
#         if l == r: return 0
#         if r - l == 1: return l
#         if r - l == 2: return l + 1
#         ans = sum(range(r))
#         for x in range(l+r>>1, r):
#             ans = min(max(self.solve(l, x-1), self.solve(x+1, r))+x, ans)
#         return ans

#     def getMoneyAmount(self, n: int) -> int:
#         return self.solve(1, n)

# import functools
# class Solution:
#     @functools.lru_cache(None)
#     def solve(self, l, r):
#         if l >= r: return 0
#         ans = float('inf')
#         for x in range(l+r>>1, r):
#             ans = min(max(self.solve(l, x-1), self.solve(x+1, r))+x, ans)
#         return ans

#     def getMoneyAmount(self, n: int) -> int:
#         return self.solve(1, n)

# from collections import deque, defaultdict

# class Solution:
#     def getMoneyAmount(self, n: int) -> int:
#         dp = defaultdict(int)
#         q = deque()
#         for i in range(1,n+1):
#             dp[i,i] = 0
#             q.append((i,i,i))
#         while q:
#             left, right, choice = q.popleft()
#             if right == n:
#                 continue
#             right += 1
#             while choice < right and dp.get((choice+1+1,right),-float('inf')) >= dp.get((left,choice+1-1),-float('inf')):
#                 choice += 1
#             dp[left,right] = min(dp.get((choice+1,right),0)+choice, dp.get((left,choice),0)+choice+1)
#             q.append((left,right,choice))
#         return dp[1,n]

from collections import deque, defaultdict

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = defaultdict(int)
        q = deque()
        for i in range(1,n+1):
            dp[i,i] = 0
            q.append((i,i))
        while q:
            left, right = q.popleft()
            if right == n:
                continue
            right += 1
            
            for choice in range(left+right>>1,right+1):
                dp[left,right] = min(dp.get((left,right),float('inf')),choice+max(dp.get((left,choice-1),0),dp.get((choice+1,right),0)))
            q.append((left,right))
        return dp[1,n]



