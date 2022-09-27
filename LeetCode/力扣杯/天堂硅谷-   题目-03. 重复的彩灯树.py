# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lightDistribution(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        seen = Counter()
        def dfs(cur):
            if not cur:
                return '#'
            left, right = dfs(cur.left), dfs(cur.right)
            v = str(cur.val)
            s = left+'-'+v+'*'+right
            s = str(hash(s))
            # print(cur,s)
            if seen[s] == 1:
                ans.append(cur)
            seen[s] += 1
            return s 
        dfs(root)
        return ans 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            tri = (node.val, dfs(node.left), dfs(node.right))
            if tri in seen:
                (tree, index) = seen[tri]
                repeat.add(tree)
                return index
            else:
                nonlocal idx
                idx += 1
                seen[tri] = (node, idx)
                return idx
        
        idx = 0
        seen = dict()
        repeat = set()

        dfs(root)
        return list(repeat)


# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/find-duplicate-subtrees/solution/xun-zhao-zhong-fu-de-zi-shu-by-leetcode-zoncw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。