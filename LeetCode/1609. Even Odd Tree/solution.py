# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q = [root]
        flag = True
        while q:
            # print([cur.val for cur in q])
            # print(flag)
            tmp = []
            for i, cur in enumerate(q):
                v = cur.val
                if (flag and v&1 == 0) or (not flag and v&1 == 1):
                    return False
                if i > 0 and ((flag and q[i].val <= q[i-1].val) or (not flag and q[i].val >= q[i-1].val)):
                    return False
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
            q = tmp
            flag = not flag
        return True