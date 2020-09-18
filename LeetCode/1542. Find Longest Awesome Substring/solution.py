class Solution:
    def longestAwesome(self, s):
        res, cur, n = 0, 0, len(s)
        seen = [-1] + [n] * 1024
        for i, c in enumerate(s):
            cur ^= 1 << int(c)
            for a in range(10):
                res = max(res, i - seen[cur ^ (1 << a)])
            res = max(res, i - seen[cur])
            seen[cur] = min(seen[cur], i)
        return res        


# class Solution:
#     def longestAwesome(self, s: str) -> int:
#         cur, res = 0, 1
#         state = {0: -1}
#         for i, ch in enumerate(s):
#             ch = int(ch)
#             cur ^= (1<<ch)
#             if cur not in state:
#                 state[cur] = i 
#             else:
#                 res = max(res,i-state[cur])
#             for k in range(10):
#                 nxt = cur ^ (1<<k)
#                 if nxt in state:
#                     res = max(res,i-state[nxt])
#         return res