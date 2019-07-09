# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# from collections import deque

# class Solution:
#     def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
#         ans = deque()
#         ans.append(root)
#         def preorder(node, val):
            
#             if node:
#                 if node.val == val:
#                     # print(node.val)
#                     if node.left:
#                         ans.append(node.left)
#                     if node.right:
#                         ans.append(node.right)
#                     return None, True
#                 node.left, flag = preorder(node.left, val)
#                 if flag:
#                     return node, True
#                 node.right, flag = preorder(node.right, val)
#                 if flag:
#                     return node, True
#                 return node, False
#             return node, False
#         for target in to_delete:
#             n = len(ans)
#             print(n)
#             for _ in range(n):
#                 tmp = ans.popleft()
#                 # print(tmp.val)
#                 tmp, flag = preorder(tmp, target)
#                 if tmp:
#                     ans.append(tmp)
#         # n = len(ans)
#         # ans_list = []
#         # for _ in range(n):
#         #     ans_list.append(ans.popleft())
#         return list(ans)


class Solution:
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root: return None
            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root
        helper(root, True)
        return res
        