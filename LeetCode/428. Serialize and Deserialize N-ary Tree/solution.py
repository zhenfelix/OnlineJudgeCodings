from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        q, res = deque(), []
        q.append(root)
        while q:
            cur = q.popleft()
            for child in cur.children:
                q.append(child)
            res.append(str(cur.val)+':'+str(len(cur.children)))
        return ','.join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        data = data.split(',')
        q = deque()
        val, cnt = map(int, data[0].split(':'))
        root = Node(val,[None]*cnt)
        q.append(root)
        idx = 0
        while q:
            cur = q.popleft()
            for i in range(len(cur.children)):
                idx += 1
                val, cnt = map(int, data[idx].split(':'))
                child = Node(val,[None]*cnt)
                cur.children[i] = child
                q.append(child)
        return root
            


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))