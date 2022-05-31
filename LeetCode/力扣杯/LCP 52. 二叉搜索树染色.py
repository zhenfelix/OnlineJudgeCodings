# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        arr = []
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            arr.append(cur.val)
            dfs(cur.right)
            return
        dfs(root)
        n = len(arr)
        # print(arr)
        m = len(ops)
        color = [0]*(m+1)
        valid = [False]*(m+1)
        openst = [[] for _ in range(n)]
        closest = [[] for _ in range(n)]
        openst[0].append(0)
        closest[-1].append(0)
        for r, (t, lo, hi) in enumerate(ops):
            left = bisect.bisect_left(arr,lo)            
            right = bisect.bisect_right(arr,hi)-1
            # print(left,right)
            if left >= n or right < 0:
                continue
            openst[left].append(r+1)
            closest[right].append(r+1)
            color[r+1] = t

        ans = 0
        hq = []
        for i in range(n):
            for r in openst[i]:
                heapq.heappush(hq, -r)
                valid[r] = True
            ans += color[-hq[0]]
            for r in closest[i]:
                valid[r] = False
            while hq and valid[-hq[0]] == False:
                heapq.heappop(hq)    
        return ans 





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
            def getnext(p):
                if not p:  return []
                return getnext(p.left) + [p.val] + getnext(p.right)
            nums = getnext(root)
            ans = 0
            for op in ops[::-1]:
                l = bisect.bisect_left(nums,op[1])
                r = bisect.bisect(nums,op[2]) - 1
                if l > r: continue 
                if op[0]==1:   ans += r - l + 1
                nums[l:r+1] = []
            return ans 

        # 作者：hxu10
        # 链接：https://leetcode-cn.com/problems/QO5KpG/solution/python-by-hxu10-mi66/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。