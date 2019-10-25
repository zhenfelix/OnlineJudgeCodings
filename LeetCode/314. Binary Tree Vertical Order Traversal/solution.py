from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        mp = defaultdict(list)
        left = float('inf')
        q = deque()
        q.append((root,0))
        while q:
            cur, idx = q.popleft()
            # if not cur:
            #     continue
            left = min(left,idx)
            mp[idx] += [cur.val]
            if cur.left: q.append((cur.left,idx-1))
            if cur.right: q.append((cur.right,idx+1))

        res = []
        while mp[left]:
            res.append(mp[left])
            left += 1

        return res