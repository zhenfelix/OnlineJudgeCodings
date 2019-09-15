# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        left, right, res = [], [], []
        cur = root
        while cur:
            if cur.val <= target:
                left.append([cur, True])
                cur = cur.right
            else:
                right.append([cur, True])
                cur = cur.left
        
        while k:
            while left and (not left[-1][-1]) and left[-1][0].right:
                left[-1][-1] = True
                left.append([left[-1][0].right, False])
            
            while right and (not right[-1][-1]) and right[-1][0].left:
                right[-1][-1] = True
                right.append([right[-1][0].left, False])
                
            
            if not right or (left and target - left[-1][0].val < right[-1][0].val - target):
                top = left.pop()
                res.append(top[0].val)
                if top[0].left:
                    left.append([top[0].left, False])
            else:
                top = right.pop()
                res.append(top[0].val)
                if top[0].right:
                    right.append([top[0].right, False])
            
            k -= 1
            
        return res


# https://tenderleo.gitbooks.io/leetcode-solutions-/GoogleHard/272.html
# class Solution:
#     def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
#         cur = root
#         stack, res = [], []
#         while cur or stack:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left
#             cur = stack.pop()
#             if len(res) < k:
#                 res.append(cur.val)
#             else:
#                 if abs(cur.val - target) < abs(target - res[-k]):
#                     res.append(cur.val)
#                 else:
#                     return res[-k:]
#             cur = cur.right
#         return res[-k:]
#                 