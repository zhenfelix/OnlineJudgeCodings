# from collections import deque

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         visited = set()
#         q = deque()
#         q.append(0)
#         visited.add(0)
#         while q:
#             front = q.popleft()
#             if front == n-1:
#                 return True
#             for x in range(1, nums[front]+1):
#                 if front+x not in visited:
#                     visited.add(front+x)
#                     q.append(front+x)
#         return False
                
from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = cur = 0
        while cur <= reach:
            reach = max(reach, nums[cur]+cur)
            cur += 1
            if reach >= n-1:
                return True
        return False
                