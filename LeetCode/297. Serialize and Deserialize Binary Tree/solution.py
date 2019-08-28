# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from collections import deque
# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         self.str = ""
#         q = deque()
#         q.append(root)
#         while len(q) > 0:
            
#             front = q.popleft()
#             if not front:
#                 self.str += "#,"
#             else:
#                 self.str += str(front.val) + ","
#                 q.append(front.left)
#                 q.append(front.right)
#         self.str = self.str[:-1]
#         # print(self.str)

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
        
#         def convert(s):
#             if s == "#":
#                 return None
#             return int(s)
        
#         q = deque()
#         idx = 1
#         arr = self.str.split(",")
#         root = None
#         tmp = convert(arr[0])
#         if tmp != None:
#             root = TreeNode(tmp)
#         q.append(root)
#         while idx < len(arr):
#             n = len(q)
#             for _ in range(n):
#                 front = q.popleft()
                
#                 tmp = convert(arr[idx])
#                 if tmp != None:
#                     left = TreeNode(tmp)
#                     front.left = left
#                     q.append(left)
#                 idx += 1
                
#                 tmp = convert(arr[idx])
#                 if tmp != None:
#                     right = TreeNode(tmp)
#                     front.right = right
#                     q.append(right)
#                 idx += 1
#         return root

class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()
                
                    
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))