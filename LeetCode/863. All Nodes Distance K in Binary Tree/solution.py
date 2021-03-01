# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def findAncestor(cur, st):
            if not cur:
                return False
            st.append(cur)
            if cur == target:
                return True
            if not findAncestor(cur.left, st) and not findAncestor(cur.right, st):
                st.pop()
                return False
            return True
        st, mp = [], {}
        findAncestor(root,st)
        st = st[::-1]
        for i, v in enumerate(st):
            mp[v] = i 
        res = []
        def dfs(cur,d):
            if not cur:
                return 
            if cur in mp:
                d = mp[cur]
            if d == K:
                res.append(cur.val)
                # return
            dfs(cur.left,d+1)
            dfs(cur.right,d+1)
            return
        dfs(root,0)
        return res 
