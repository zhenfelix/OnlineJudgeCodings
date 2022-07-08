"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def moveSubTree(self, root: 'Node', u: 'Node', v: 'Node') -> 'Node':
        parent = dict()
        tin, tout = dict(), dict()
        clock = 0
        def dfs(cur, p = None):
            nonlocal clock
            if cur == u or cur == v:
                parent[cur] = p 
            clock += 1
            tin[cur.val] = clock
            for nxt in cur.children:
                dfs(nxt, cur)
            clock += 1
            tout[cur.val] = clock
            return
        dfs(root)

        def isAncestor(x,y):
            return tin[x.val] < tin[y.val] and tout[x.val] > tout[y.val]

        def replace(p,x,y):
            tmp = []
            for c in p.children:
                if c == x:
                    tmp.append(y)
                else:
                    tmp.append(c)
            p.children = tmp
            return

        def remove(p,x):
            tmp = []
            for c in p.children:
                if c != x:
                    tmp.append(c)
            p.children = tmp
            return

        if isAncestor(u,v):
            if parent[u]:
                replace(parent[u],u,v)
            else:
                root = v
            remove(parent[v],v)
            v.children.append(u)
        elif parent[u] != v:
            remove(parent[u],u)
            v.children.append(u)
        return root

