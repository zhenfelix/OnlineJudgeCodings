# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inOrder(cur, res):
            if cur:
                inOrder(cur.left, res)
                res.append(cur.val)
                inOrder(cur.right, res)

        res1, res2 = [], []
        inOrder(root1, res1)
        inOrder(root2, res2)
        return sorted(res1+res2)


# - [Why is Python generator-based inorder traversal so slow?](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/discuss/464167/Why-is-Python-generator-based-inorder-traversal-so-slow)
# import heapq

# class Solution:
#     def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#         def gen(node):
#             if node:
#                 yield from gen(node.left)
#                 yield node.val
#                 yield from gen(node.right)
#         return list(heapq.merge(gen(root1), gen(root2)))