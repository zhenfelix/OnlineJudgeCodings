# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def countPairs(self, root: TreeNode, distance: int) -> int:
#         count = 0
#         ans=0
#         def dfs(node):
#             nonlocal ans
#             if not node:
#                 return []
#             if not node.left and not node.right:
#                 return [1]
#             left=dfs(node.left)
#             right=dfs(node.right)
#             if left and right:
#                 for le in left:
#                     for ri in right:
#                         if le+ri<=distance:
#                             ans+=1
#             return [n+1 for n in left+right if n+1<=distance]
#         dfs(root)
#         return ans

# class Solution:
#     def countPairs(self, root: TreeNode, distance: int) -> int:
#         def dfs(cur):
#             if not cur:
#                 return 0, []
#             if not cur.left and not cur.right:
#                 return 0, [0]
#             cnt = 0
#             c1, depth1 = dfs(cur.left)
#             cnt += c1
#             c2, depth2 = dfs(cur.right)
#             cnt += c2 
#             depth1 = [d+1 for d in depth1]
#             depth2 = [d+1 for d in depth2]
#             if not depth1:
#                 # print(cur.val, c2)
#                 return cnt, depth2
#             if not depth2:
#                 # print(cur.val, c1)
#                 return cnt, depth1
#             n1, n2 = len(depth1), len(depth2)

#             j = n2-1
#             for i in range(n1):
#                 while j >= 0 and depth1[i]+depth2[j] > distance:
#                     j -= 1
#                 cnt += j+1
#             # print(cur.val, cnt)
#             return cnt, sorted([x for x in depth1+depth2 if x <= distance])
#             # return cnt, sorted([x for x in depth1+depth2])
#         return dfs(root)[0]

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0
        def dfs(node):
            if not node: return Counter()
            if not node.left and not node.right:
                return Counter([0])
            lcount = dfs(node.left)
            rcount = dfs(node.right)
            for ld,ln in lcount.items():
                for rd,rn in rcount.items():
                    if ld+rd+2<=distance: self.res += ln*rn
            return Counter({k+1:v for k,v in (lcount+rcount).items() if k < distance})
        dfs(root)
        return self.res