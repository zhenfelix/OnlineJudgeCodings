# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minimalExecTime(self, root: TreeNode) -> float:
        def dfs(cur):
            if not cur:
                return 0, 0
            p1, s1 = dfs(cur.left)
            p2, s2 = dfs(cur.right)
            if s1 < s2:
                s1, p1, s2, p2 = s2, p2, s1, p1
            if s1-2*p1 <= s2:
                return (s1+s2)/2, s1+s2+cur.val
            return p1+s2, s1+s2+cur.val
        p, s = dfs(root)
        return s-p



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minimalExecTime(self, root: TreeNode) -> float:
        def dfs(cur):
            if not cur:
                return 0, 0
            t1, s1 = dfs(cur.left)
            t2, s2 = dfs(cur.right)
            return max(t1,t2,(s1+s2)/2)+cur.val, s1+s2+cur.val
        return dfs(root)[0]