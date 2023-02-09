class Solution:
    def countTime(self, time: str) -> int:
        return sum(all(p in (q,'?') for p, q in zip(time,f'{h:02d}:{m:02d}')) for h in range(24) for m in range(60)) 


# class Solution:
#     def countTime(self, time: str) -> int:
#         def check(s):
#             hh, mm = s.split(':')
#             return '00' <= hh < '24' and '00' <= mm < '60'
#         arr = list(time)
#         ans = 0
#         def dfs(i):
#             nonlocal ans
#             if i == 5:
#                 if check(''.join(arr)):
#                     # print(arr)
#                     ans += 1
#                 return
#             if time[i] == '?':
#                 for ch in range(10):
#                     arr[i] = str(ch)
#                     dfs(i+1)
#             else:
#                 dfs(i+1)
#             return 
#         dfs(0)
#         return ans 
