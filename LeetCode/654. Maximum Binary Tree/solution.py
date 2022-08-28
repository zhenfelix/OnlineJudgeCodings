# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        nums.append(math.inf)
        n = len(nums)
        nodes = [TreeNode(nums[i]) for i in range(n)]
        st = [-1]
        for i in range(n):
            while nums[st[-1]] < nums[i]:
                j = st.pop()
                if nums[st[-1]] < nums[i]:
                    nodes[st[-1]].right = nodes[j]
                else:
                    nodes[i].left = nodes[j]
            st.append(i)
        # print(nodes)
        return nodes[-1].left