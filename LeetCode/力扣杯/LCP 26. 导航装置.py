# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def navigation(self, root: TreeNode) -> int:
        leaves = []
        g = defaultdict(list)
        def dfs(cur, parent):
            if parent: 
                g[cur].append(parent)
                g[parent].append(cur)
            if cur.left:
                dfs(cur.left, cur)
            if cur.right:
                dfs(cur.right, cur)
            if len(g[cur]) == 1:
                leaves.append(cur)
            return
        
        dfs(root, None)
        if len(leaves) == 2:
            return 1
            
        visited = set()
        removed = set()

        def dfs2(cur):
            visited.add(cur)
            if len(g[cur]) == 3:
                removed.add(cur)
                return
            for nxt in g[cur]:
                if nxt not in visited:
                    dfs2(nxt)

        for x in leaves:
            if x not in visited:
                dfs2(x)
        # print(branch)
        return len(leaves) - len(removed)