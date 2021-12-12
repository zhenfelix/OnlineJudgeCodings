# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# import sys
# sys.setrecursionlimit(10**6)

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        g = defaultdict(lambda : [-1,-1,-1])
        def dfs(cur,parentv,isleft):
            if not cur:
                return
            curv = cur.val
            if parentv > 0:
                g[curv][2] = parentv
                if isleft:
                    g[parentv][0] = curv
                else:
                    g[parentv][1] = curv
            dfs(cur.left, curv, True)
            dfs(cur.right, curv, False)
            return
        dfs(root,0,True)

        dirs = "LRU"
        visited = defaultdict(lambda : ("",0))
        q = deque()
        q.append(startValue)
        while (q):
            cur = q.popleft()
            if cur == destValue:
                break
            for i, nxt in enumerate(g[cur]):
                if nxt > 0 and nxt not in visited:
                    visited[nxt] = (dirs[i],cur)
                    q.append(nxt)
        res = []
        cur = destValue
        while cur != startValue:
            res.append(visited[cur][0])
            cur = visited[cur][1]
        return ''.join(res)[::-1]



class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def lca(node): 
            """Return lowest common ancestor of start and dest nodes."""
            if not node or node.val in (startValue , destValue): return node 
            left, right = lca(node.left), lca(node.right)
            return node if left and right else left or right
        
        root = lca(root) # only this sub-tree matters
        
        def fn(val): 
            """Return path from root to node with val."""
            stack = [(root, "")]
            while stack: 
                node, path = stack.pop()
                if node.val == val: return path 
                if node.left: stack.append((node.left, path + "L"))
                if node.right: stack.append((node.right, path + "R"))
        
        path0 = fn(startValue)
        path1 = fn(destValue)
        return "U"*len(path0) + path1