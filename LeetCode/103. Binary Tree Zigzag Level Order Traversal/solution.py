# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        st1, st2 = [], []
        ans = []
        if root:
            st1 += [root]
        
        while len(st1) > 0:
            tmp = []
            while len(st1) > 0:
                p = st1.pop()
                tmp += [p.val]
                if p.left: 
                    st2 += [p.left]
                if p.right: 
                    st2 += [p.right]
            ans += [tmp]
            
            if len(st2) == 0:
                break
            tmp = []
            while len(st2) > 0:
                p = st2.pop()
                tmp += [p.val]
                if p.right:
                    st1 += [p.right]
                if p.left:
                    st1 += [p.left]
            ans += [tmp]
        
        return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, st = [], [root]
        flag = -1
        while st:
            n = len(st)
            res.append([])
            tmp = []
            for _ in range(n):
                cur = st.pop()
                res[-1].append(cur.val)
                left, right = cur.left, cur.right
                if flag == 1:
                    left, right = right, left
                if left:
                    tmp.append(left)
                if right:
                    tmp.append(right)
            st = tmp
            flag *= (-1)
        return res

