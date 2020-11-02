# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        seen = defaultdict(list)
        def dfs(cur):
            if not cur:
                return '#'
            left, right = dfs(cur.left), dfs(cur.right)
            # s = str(cur.val) + ',' + left + ',' + right
            s = left + ',' + right + ',' + str(cur.val)
            seen[s].append(cur)
            return s
        dfs(root)
        # print(seen.keys())
        return [v[0] for k,v in seen.items() if len(v) > 1]