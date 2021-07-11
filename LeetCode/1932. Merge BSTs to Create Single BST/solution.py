# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        mp = {}
        for i, root in enumerate(trees):
            mp[root.val] = root
        indegree = Counter()
        def dfs(cur, root):
            if not cur.left and not cur.right:
                if cur != root and cur.val in mp:
                    indegree[cur.val] += 1
                return
            if cur.left:
                dfs(cur.left, root)
            if cur.right:
                dfs(cur.right, root)
            return

        for i, root in enumerate(trees):
            dfs(root, root)

        res = None
        for i, root in enumerate(trees):
            if indegree[root.val] > 1:
                return None
            if indegree[root.val] == 0:
                if not res:
                    res = root
                else:
                    return None
        if not res:
            return None
        cnt = [1]
        def buildTree(cur):
            if not cur.left and not cur.right:
                if cur.val in mp and cur != mp[cur.val]:
                    cnt[0] += 1
                    cur, flag, lo, hi = buildTree(mp[cur.val])
                    return cur, flag, lo, hi 
                else:
                    return cur, True, cur.val, cur.val
            flag = True
            lo = hi = cur.val
            if cur.left:
                cur.left, tmp, lo, hi_ = buildTree(cur.left)
                flag &= tmp
                flag &= (hi_ < cur.val)
            if cur.right:
                cur.right, tmp, lo_, hi = buildTree(cur.right)
                flag &= tmp
                flag &= (cur.val < lo_)
            return cur, flag, lo, hi 
        res, flag, lo, hi = buildTree(res)
        if cnt[0] != len(trees):
            return None
        return res if flag else None