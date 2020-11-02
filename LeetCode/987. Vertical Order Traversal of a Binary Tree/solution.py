# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
#         mp = defaultdict(list)
#         def dfs(cur,x,y):
#             if not cur: return
#             mp[x,y].append(cur.val)
#             dfs(cur.left,x-1,y+1)
#             dfs(cur.right,x+1,y+1)
#         dfs(root,0,0)
#         res = []
#         arr = [(x,y,v) for x,y in mp for v in mp[x,y]]
#         arr.sort()
#         # print(arr)
#         for i, (x,y,v) in enumerate(arr):
#             if not res or arr[i][0] != arr[i-1][0]:
#                 res.append([])
#             res[-1].append(v)
#         return res


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        q = []
        def dfs(cur,x,y):
            if not cur: return
            q.append((x,y,cur.val))
            dfs(cur.left,x-1,y+1)
            dfs(cur.right,x+1,y+1)
        dfs(root,0,0)
        heapq.heapify(q)
        res = []
        pre = None
        while q:
            x, y, v = heapq.heappop(q)
            if pre == None or pre != x:
                res.append([])
            res[-1].append(v)
            pre = x 
        return res
