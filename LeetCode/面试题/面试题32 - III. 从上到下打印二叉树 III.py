# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, st = [], [root]
        flag = -1
        while st:
            n = len(st)
            res.append([])
            tmp = []
            for _ in range(n):
                cur = st.pop()
                res[-1].append(cur.val)
                left, right = cur.left, cur.right
                if flag == 1:
                    left, right = right, left
                if left:
                    tmp.append(left)
                if right:
                    tmp.append(right)
            st = tmp
            flag *= (-1)
        return res
