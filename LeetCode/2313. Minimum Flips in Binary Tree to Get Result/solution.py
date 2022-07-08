# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        def calc(a,b,op):
            if op == 2:
                return a|b  
            elif op == 3:
                return a&b 
            else:
                return a^b

        if root.val <= 1:
            return int(root.val != result) 
        if root.val == 5:
            if root.left:
                return self.minimumFlips(root.left, not result)
            else:
                return self.minimumFlips(root.right, not result)
        res = float('inf')
        for a, b in product([0,1], repeat=2):
            if calc(a,b,root.val) == result:
                res = min(res, self.minimumFlips(root.left, a)+self.minimumFlips(root.right,b))
        return res 
