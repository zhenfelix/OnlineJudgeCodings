# from functools import lru_cache
# class Solution:
#     def minimumTime(self, s: str) -> int:
#         n = len(s)
#         presums = [0]
#         for ch in s:
#             presums.append(presums[-1]+int(ch))

#         q = deque()
#         for sz in range(n+1):
#             while q and presums[q[-1]]*2+n-q[-1] >= presums[sz]*2+n-sz:
#                 q.pop()
#             q.append(sz)
#         # print(presums,q)
#         res = float('inf')
#         for sz in range(n+1):
#             if sz > q[0]:
#                 q.popleft()
#             res = min(res, sz+(presums[q[0]]-presums[sz])*2+(n-q[0]))

#         return res


class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        for i in range(n)[::-1]:
            dp[i] = min(dp[i+1]+int(s[i])*2, n-i)

        return min(i+dp[i] for i in range(n+1))