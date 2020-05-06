# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
#         def cmp(idx, cur):
#             if not idx:
#                 return True
#             if not cur:
#                 return False
#             flag = idx.val == cur.val and (cmp(idx.next,cur.left) or cmp(idx.next,cur.right))
#             # print("cmp",idx.val,cur.val,flag)
#             return flag
#         def dfs(idx, cur):
#             if not idx:
#                 return True
#             if not cur:
#                 return False
#             flag = cmp(idx,cur) or dfs(idx,cur.left) or dfs(idx,cur.right)
#             # print("dfs",idx.val,cur.val,flag)
#             return flag
#         return dfs(head,root)

class Solution:
    def dfs(self, head, root):
            if not head: return True
            if not root: return False
            return root.val == head.val and (self.dfs(head.next, root.left) or self.dfs(head.next, root.right))
        
    def isSubPath(self, head, root):
        if not head: return True
        if not root: return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


from functools import lru_cache
class Solution:
    def kmp(self, s):
        n = len(s)
        nxt = [-1]*(n+1)
        i, j = 0, -1
        while i < n:
            if j == -1 or s[i] == s[j]:
                i += 1
                j += 1
                nxt[i] = j
            else:
                j = nxt[j]
        return nxt

    def isSubPath(self, head, root):
        s = []
        while head:
             s.append(head.val)
             head = head.next
        nxt = self.kmp(s)
        m = len(s)
        @lru_cache(None)
        def dfs(cur, state):
            if state == m:
                return True
            if not cur:
                return False
            while state != -1 and cur.val != s[state]:
                state = nxt[state]
            state += 1
            return dfs(cur.left, state) or dfs(cur.right, state)

        return dfs(root, 0)

