# class Solution:
#     def minWindow(self, s1: str, s2: str) -> str:
#         n, m = len(s1), len(s2)
#         state = [0 if s1[i] != s2[0] else 1 for i in range(n)] 
#         start = [-float('inf') if s1[i] != s2[0] else i for i in range(n)]
        
#         for j in range(1,m):
#             cur = -float('inf')
#             for i in range(n):
#                 if state[i] == j:
#                     nxt = start[i]
#                 else:
#                     nxt = cur
#                 if s2[j] == s1[i] and cur >= 0:
#                     start[i] = cur
#                     state[i] = j+1
#                 cur = nxt
#             # print(start,state)
#         ans = -1
#         start.append(-float('inf'))
#         for i in range(n):
#             if state[i] == m and i-start[i] < ans-start[ans]:
#                 ans = i 
#         if ans >= 0:
#             return s1[start[ans]:ans+1]
#         return ""




class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        dp = [-float('inf')]
        ans = [-float('inf'), float('inf')]
        for i, ch in enumerate(s1):
            dp[0] = i
            for j in range(m)[::-1]:
                if s2[j] == ch:
                    dp[j+1] = dp[j]
            if i-dp[m] < ans[-1]-ans[0]:
                ans = [dp[m],i]
        
        if ans[0] >= 0:
            return s1[ans[0]:ans[-1]+1]
        return ""
