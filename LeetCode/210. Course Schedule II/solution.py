# from collections import deque

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         ans = []
#         dq = deque()
#         mp = {}
#         incoming = [0]*numCourses
#         for i in range(numCourses):
#             mp[i] = []
#         for p in prerequisites:
#             mp[p[1]] += [p[0]]
#             incoming[p[0]] += 1
        
#         for idx, ic in enumerate(incoming):
#             if ic == 0:
#                 dq.append(idx)
        
#         while len(dq) > 0:
#             front = dq.popleft()
#             ans += [front]
#             for node in mp[front]:
#                 incoming[node] -= 1
#                 if incoming[node] == 0:
#                     dq.append(node)
        
#         if len(ans) < numCourses:
#             return []
#         return ans
        
        
        

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        mp = {}
        WHITE, GRAY, BLACK = 0, 1, 2
        colors = [WHITE]*numCourses
        for i in range(numCourses):
            mp[i] = []
        for p in prerequisites:
            mp[p[1]] += [p[0]]
        def dfs(node):
            if colors[node] == BLACK:
                return True
            elif colors[node] == GRAY:
                return False
            else:
                colors[node] = GRAY
            for child in mp[node]:
                if not dfs(child):
                    return False
            colors[node] = BLACK
            ans.append(node)
            return True
        
        for idx in range(numCourses):
            if not dfs(idx):
                return []
        return ans[::-1]
        
        
        
        