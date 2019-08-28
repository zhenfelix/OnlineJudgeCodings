# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        st1, st2 = [], []
        ans = []
        if root:
            st1 += [root]
        
        while len(st1) > 0:
            tmp = []
            while len(st1) > 0:
                p = st1.pop()
                tmp += [p.val]
                if p.left: 
                    st2 += [p.left]
                if p.right: 
                    st2 += [p.right]
            ans += [tmp]
            
            if len(st2) == 0:
                break
            tmp = []
            while len(st2) > 0:
                p = st2.pop()
                tmp += [p.val]
                if p.right:
                    st1 += [p.right]
                if p.left:
                    st1 += [p.left]
            ans += [tmp]
        
        return ans
