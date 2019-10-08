# class Solution:
#     def countSteppingNumbers(self, low: int, high: int) -> List[int]:
#         def dfs(n, idx, tmp):
#             if n == 1:
#                 for i in range(10):
#                     if i >= low and i <= high:
#                         ans.append(i)
#                 return
            
#             if idx == n:
#                 i = int(tmp)
#                 if i >= low and i <= high:
#                     ans.append(i)
#                 return
            
#             if idx == 0:
#                 for i in range(1,10):
#                     dfs(n,idx+1,str(i))
#             else:
#                 last = int(tmp[-1])
#                 if last > 0:
#                     dfs(n,idx+1,tmp+str(last-1))
#                 if last < 9:
#                     dfs(n,idx+1,tmp+str(last+1))
#             return
        
#         ans = []
#         for digit in range(1,11):
#             # print(digit)
#             dfs(digit,0,"")
#         return ans

from collections import deque

class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        q = deque()
        ans = []
        for i in range(1,10):
            q.append(i)
        if low == 0:
            ans.append(0)
        while q:
            front = q.popleft()
            if front <= high:
                if front >= low:
                    ans.append(front)
                last = front%10
                if last > 0:
                    q.append(front*10+last-1)
                if last < 9:
                    q.append(front*10+last+1)
        return ans
