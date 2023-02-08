# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            arr.append(cur.val)
            dfs(cur.right)
            return
        dfs(root)
        n = len(queries)
        ans = [[-1,-1] for _ in range(n)]
        m = len(arr)
        for i, v in enumerate(queries):
            idx = bisect_right(arr, v)-1
            if idx >= 0:
                ans[i][0] = arr[idx]
            idx = bisect_left(arr, v)
            if idx < m:
                ans[i][1] = arr[idx]
        return ans 



class Solution:

    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:

        a = []

        def dfs(o: Optional[TreeNode]) -> None:

            if o is None: return

            dfs(o.left)

            a.append(o.val)

            dfs(o.right)

        dfs(root)



        ans = []

        for q in queries:

            j = bisect_right(a, q)

            min = a[j - 1] if j else -1

            j = bisect_left(a, q)

            max = a[j] if j < len(a) else -1

            ans.append([min, max])

        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/solutions/1981349/zhong-xu-bian-li-er-fen-cha-zhao-by-endl-m8ez/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。