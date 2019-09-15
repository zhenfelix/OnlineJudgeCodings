# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         st = []
#         if not root:
#             return res
#         dummy = TreeNode(-1)
#         # dummy.left = TreeNode(-1)
#         dummy.right = root
#         st.append([dummy,dummy.right])
#         while st:
#             if len(st[-1]) == 1:
#                 res.append(st.pop()[0].val)
#             else:
#                 cur = st[-1].pop()
#                 st.append([cur])
#                 if cur.right:
#                     st[-1].append(cur.right)
#                 if cur.left:
#                     st[-1].append(cur.left)
                
#         return res[:-1]

# class Solution: #栈的精髓：把 递归中最后处理 的 压在最前面 
#     def postorderTraversal(self, root: TreeNode) -> List[int]:  
#         if not root: return []
        
#         res = []
#         stack = [(root, False)]
#         while stack:
#             node, expanded = stack.pop()
#             if expanded:
#                 res.append(node.val)
#             else:
#                 stack.append((node, True))
#                 if node.right:
#                     stack.append((node.right, False))
#                 if node.left:
#                     stack.append((node.left, False))
                
#         return res

class Solution: 
    def postorderTraversal(self, root: TreeNode) -> List[int]:  
        if not root: return []
        
        res = []
        stack = []
        last = None
        child = root
        # dummy = TreeNode(-1)
        # dummy.left = root
        # stack.append(dummy)
        while stack or child:
            if child:
                stack.append(child)
                child = child.left
            else:
                if stack[-1].right and last != stack[-1].right:
                    # stack.append(node.right)
                    child = stack[-1].right
                else:
                    last = stack.pop()
                    res.append(last.val)
                
        return res
                