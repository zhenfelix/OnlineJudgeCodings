# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        arr = []
        def dfs(cur,d):
            if not cur:
                return
            if len(arr) == d:
                arr.append([])
            arr[d].append(cur.val)
            dfs(cur.left,d+1)
            dfs(cur.right,d+1)
            return 
        dfs(root,0)

        def check(nums):
            cnt = 0
            n = len(nums)
            target = sorted(nums)
            mp = {v:i for i, v in enumerate(target)}
            visited = [False]*n 
            for i in range(n):
                if not visited[i]:
                    j = i 
                    cc = 0
                    while not visited[j]:
                        cc += 1
                        visited[j] = True
                        j = mp[nums[j]]
                    cnt += cc-1
            return cnt
        ans = 0
        for a in arr:
            ans += check(a)
        return ans 