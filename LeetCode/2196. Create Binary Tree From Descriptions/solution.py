# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = dict()
        pcnt = set()
        for p, child, isleft in descriptions:
            pcnt.add(child)
            if p not in mp:
                mp[p] = TreeNode(p)
            if child not in mp:
                mp[child] = TreeNode(child)
            if isleft:
                mp[p].left = mp[child]
            else:
                mp[p].right = mp[child]
        for r in mp.keys():
            if r not in pcnt:
                return mp[r]
        return None

