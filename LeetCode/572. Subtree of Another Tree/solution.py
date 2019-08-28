# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
    
#     def isSame(self, a, b):
#         if not a or not b:
#             return a == None and b == None
#         return a.val == b.val and self.isSame(a.left, b.left) and self.isSame(a.right, b.right)
    
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         if not s:
#             return t == None
#         if not t:
#             return True
#         return self.isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

# class Solution:
# 	def isSubtree(self, s, t):
# 	    from hashlib import sha256
# 	    def hash_(x):
# 	        S = sha256()
# 	        S.update(x)
# 	        return S.hexdigest()
	        
# 	    def merkle(node):
# 	        if not node:
# 	            return '#'
# 	        m_left = merkle(node.left)
# 	        m_right = merkle(node.right)
# 	        node.merkle = hash_((m_left + str(node.val) + m_right).encode('utf-8'))
# 	        return node.merkle
	        
# 	    merkle(s)
# 	    merkle(t)
# 	    def dfs(node):
# 	        if not node:
# 	            return False
# 	        return (node.merkle == t.merkle or 
# 	                dfs(node.left) or dfs(node.right))
	                    
# 	    return dfs(s)

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"
        
        return convert(t) in convert(s)
