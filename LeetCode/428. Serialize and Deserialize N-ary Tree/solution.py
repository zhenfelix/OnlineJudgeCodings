"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        arr = []
        def dfs(cur):
            if not cur:
                return
            arr.append(cur.val)
            arr.append('[')
            for nxt in cur.children[::-1]:
                dfs(nxt)
            arr.append(']')
        dfs(root)
        # print(arr)
        return ','.join(map(str,arr))
        
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        arr = data.split(',')
        arr = [Node(int(x),[]) if x not in "[]" else x for x in arr]
        st = []
        for cur in arr:
            if cur == '[':
                st.append('[')
            elif cur == ']':
                tmp = []
                while st[-1] != '[':
                    tmp.append(st.pop())
                st.pop()
                st[-1].children = tmp
            else:
                st.append(cur)
        return st[-1]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return '#'
        arr = []
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            if not cur:
                arr.append('#')
                continue
            arr.append(cur.val)
            for nxt in cur.children:
                q.append(nxt)
            q.append(None)
        return ','.join(map(str,arr))
        
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if data == '#':
            return None
        nq = deque(data.split(','))
        q = deque()
        root = Node(int(nq.popleft()),[])
        q.append(root)
        while q:
            cur = q.popleft()
            while nq:
                nxt = nq.popleft()
                if nxt == '#':
                    break
                nxt = Node(int(nxt),[])
                q.append(nxt)
                cur.children.append(nxt)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))









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