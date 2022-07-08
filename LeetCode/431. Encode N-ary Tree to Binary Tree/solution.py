"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

def __str__(self):
    return str(self.val)



class Codec:
    def __init__(self):
        Node.__repr__ = __str__
        TreeNode.__repr__ = __str__

    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None
        # print(root)
        troot = TreeNode(root.val)
        pre = None
        for c in root.children:
            cur = self.encode(c)
            if pre:
                pre.right = cur
            else: 
                troot.left = cur
            pre = cur 
        return troot

    def _decode(self, data: TreeNode, parent = None) -> 'Node':
        if not data:
            return None
        # print(data)
        root = Node(data.val, [])
        if parent:
            parent.children.append(root)
        self._decode(data.left, root)
        self._decode(data.right, parent)
        return root

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None
        return self._decode(data)

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

def __str__(self):
    return str(self.val)



class Codec:
    def __init__(self):
        Node.__repr__ = __str__
        TreeNode.__repr__ = __str__


    def bfs(self, root, binary = True):
        arr = []
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            arr.append(cur)
            if not cur:
                continue
            if binary:
                q.append(cur.left)
                q.append(cur.right)
            else:
                for nxt in cur.children:
                    q.append(nxt)
                q.append(None)
        return deque(arr)

    def tree(self, nq, binary = True):
        q = deque()
        if binary:
            root = TreeNode(nq.popleft().val)
        else:
            root = Node(nq.popleft().val, [])
        q.append(root)
        while q:
            cur = q.popleft()
            # print(cur, q, nq)
            if binary:
                if nq:
                    l = nq.popleft()
                    if l:
                        l = TreeNode(l.val)
                        q.append(l)
                    cur.left = l 
                if nq:
                    r = nq.popleft()
                    if r:
                        r = TreeNode(r.val)
                        q.append(r)
                    cur.right = r 
            else:
                while nq:
                    child = nq.popleft()
                    if not child:
                        break
                    child = Node(child.val, [])
                    cur.children.append(child)
                    q.append(child)
        return root


    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None 
        nq = self.bfs(root, False)
        # print(nq)
        return self.tree(nq)
    
    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None
        nq = self.bfs(data)
        # print(nq)
        return self.tree(nq, False)

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))



"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    def __init__(self):
        self.cc = []
        self.head = TreeNode()

    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None
        q = [root]
        data = self.head
        while q:
            nq = []
            for cur in q:
                data.right = TreeNode(cur.val)
                data = data.right
                self.cc.append(len(cur.children))
                for nxt in cur.children:
                    nq.append(nxt)
            q = nq
        return self.head.right
    
    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None
        cur = data.right
        root = Node(data.val,[])
        q = deque([root])
        idx = 0
        while cur:
            ncur = q.popleft()
            while cur and (len(ncur.children) < self.cc[idx]):
                ncur.children.append(Node(cur.val,[]))
                q.append(ncur.children[-1])
                cur = cur.right
            idx += 1
        return root

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))