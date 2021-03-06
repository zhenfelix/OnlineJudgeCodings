# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def rightSideView(self, root: TreeNode) -> List[int]:
#         q=collections.deque()
#         if root==None: return []
#         q.appendleft(root)
#         ans=[]
#         cur_count=1
#         next_count=0
#         while cur_count>0:
#             node=q.pop()
            
#             if node.left!=None:
#                 q.appendleft(node.left)
#                 next_count+=1
#             if node.right!=None:
#                 q.appendleft(node.right)
#                 next_count+=1
#             if cur_count==1:
#                 ans.append(node.val)
#                 cur_count=next_count
#                 next_count=0
#             else:
#                 cur_count-=1

#         return ans

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        results=[]
        q=deque()
        q.append(root)
        while len(q)>0:
            # bfs
            results.append(q[-1].val)
            for _ in range(len(q)):
                n=q.popleft()
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
        return results
                

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = [root]
        res = []
        while q:
            print(q)
            res.append(q[-1].val)
            tmp = []
            for cur in q:
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
            q = tmp
        return res