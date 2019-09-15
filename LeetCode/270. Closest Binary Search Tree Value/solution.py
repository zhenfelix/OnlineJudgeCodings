# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        left, right = -float('inf'), float('inf')
        cur = root
        while cur:
            if cur.val <= target:
                left = cur.val
                cur = cur.right
            else:
                right = cur.val
                cur = cur.left
        if target-left < right - target:
            return left
        else:
            return right