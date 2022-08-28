# find start's ancestors 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans = 0
        sdepth = 0
        slevel = 0
        def dfs(cur, level):
            nonlocal ans, sdepth, slevel
            if not cur:
                return -1
            l = dfs(cur.left, level+1)
            r = dfs(cur.right, level+1)
            if cur.val == start:
                sdepth = max(l,r)+1
                slevel = level
                ans = sdepth
                return -2
            tmp = max(l,r)+1
            if l == -2:
                ans = max(ans, max(r+1+slevel-level,sdepth))
                tmp = -2
            if r == -2:
                ans = max(ans, max(l+1+slevel-level,sdepth))
                tmp = -2
            
            return tmp
        dfs(root,0)
        return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans = 0
        sdepth = 0
        def dfs(cur):
            nonlocal ans, sdepth
            if not cur:
                return -1, -1
            ldepth, ldelta = dfs(cur.left)
            rdepth, rdelta = dfs(cur.right)
            if cur.val == start:
                sdepth = max(ldepth,rdepth)+1
                ans = sdepth
                return sdepth, 0
            if ldelta >= 0:
                ans = max(ans,max(sdepth, ldelta+1+rdepth+1))
                ldelta += 1
            rdepth += 1
            if rdelta >= 0:
                ans = max(ans,max(sdepth, rdelta+1+ldepth+1))
                rdelta += 1
            ldepth += 1
            # print(cur.val,max(ldepth,rdepth), max(ldelta,rdelta))
            return max(ldepth,rdepth), max(ldelta,rdelta)
        dfs(root)
        return ans




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = defaultdict(list)
        def dfs(cur):
            if cur.left:
                left = cur.left
                g[cur.val].append(left.val)
                g[left.val].append(cur.val)
                dfs(left)
            if cur.right:
                right = cur.right
                g[cur.val].append(right.val)
                g[right.val].append(cur.val)
                dfs(right)
            return

        dfs(root)
        visited = set()
        visited.add(start)
        q = [start]
        cnt = -1
        while q:
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    if nxt not in visited:
                        nq.append(nxt)
                        visited.add(nxt)
            q = nq 
            cnt += 1
        return cnt

