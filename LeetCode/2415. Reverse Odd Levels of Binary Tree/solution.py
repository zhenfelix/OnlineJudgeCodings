# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q, level = [root], 0
        while q and q[0].left:
            q = list(chain.from_iterable((node.left, node.right) for node in q))
            if level == 0:
                for i in range(len(q) // 2):
                    x, y = q[i], q[len(q) - 1 - i]
                    x.val, y.val = y.val, x.val
            level ^= 1
        return root


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/reverse-odd-levels-of-binary-tree/solution/zhi-jie-jiao-huan-zhi-by-endlesscheng-o8ze/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        ans = []
        level = 0
        while q:
            if level&1:
                ans.append(q[::-1])
            else:
                ans.append(q[:])
            nq = []
            for cur in q:
                if cur.left:
                    nq.append(cur.left)
                if cur.right:
                    nq.append(cur.right)
            q = nq
            level += 1
        for cur, nxt in zip(ans[:-1],ans[1:]):
            n = len(cur)
            for i in range(n):
                cur[i].left = nxt[i*2]
                cur[i].right = nxt[i*2+1]
        return root