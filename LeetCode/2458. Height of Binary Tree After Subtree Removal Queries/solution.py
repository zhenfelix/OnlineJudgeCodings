class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height, depth = dict(), dict()
        peer = defaultdict(lambda: [0, 0])
        def dfs(node: TreeNode, d=0):
            if node is None: return 0
            depth[node.val] = d
            height[node.val] = t = 1 + max(dfs(node.left, d + 1), dfs(node.right, d + 1))
            if t > peer[d][0]: t, peer[d][0] = peer[d][0], t
            if t > peer[d][1]: peer[d][1] = t
            return height[node.val]
            
        dfs(root)
        return [height[root.val] - 1 - (0 if height[u] != peer[depth[u]][0] else height[u] - peer[depth[u]][1]) for u in queries]


# 作者：FreeYourMind
# 链接：https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/solution/by-freeyourmind-92hr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        arr = []
        left, right, depth = dict(), dict(), dict()
        def dfs(cur,d):
            depth[cur.val] = d 
            if not cur.left and not cur.right:
                v = cur.val
                left[v] = len(arr)
                right[v] = len(arr)
                arr.append(d)
                return left[v], right[v]
            l, r = float('inf'), -float('inf')
            if cur.left:
                nl, nr = dfs(cur.left, d+1)
                l = min(l, nl)
                r = max(r, nr)
            if cur.right:
                nl, nr = dfs(cur.right, d+1)
                l = min(l, nl)
                r = max(r, nr)
            v = cur.val
            left[v] = l 
            right[v] = r 
            return l, r
        dfs(root, 0)

        # print(left,right)
        n = len(arr)
        prefix, suffix = [0]*n, [0]*n 
        ans = []
        for i in range(n):
            prefix[i] = max(prefix[i-1], arr[i])
        for i in range(n)[::-1]:
            suffix[i] = max(suffix[(i+1)%n], arr[i])
        for q in queries:
            mx = depth[q]-1
            l, r = left[q], right[q]
            if l > 0:
                mx = max(mx, prefix[l-1])
            if r < n-1:
                mx = max(mx, suffix[r+1])
            ans.append(mx)
        return ans 



class SegmentTree:
    def __init__(self, data, merge=max): 
        '''
        data:传入的数组
        merge:处理的业务逻辑，例如求和/最大值/最小值，lambda表达式
        '''

        self.data = data
        self.n = len(data)
        #  申请4倍data长度的空间来存线段树节点
        self.tree = [None] * (4 * self.n) # 索引i的左孩子索引为2i+1，右孩子为2i+2
        self._merge = merge
        if self.n:
            self._build(0, 0, self.n-1)


    def query(self, ql, qr):
        '''
        返回区间[ql,..,qr]的值
        '''
        return self._query(0, 0, self.n-1, ql, qr)

    def update(self, index, value):
        # 将data数组index位置的值更新为value,然后递归更新线段树中被影响的各节点的值
        self.data[index] = value
        self._update(0, 0, self.n-1, index)

    def _build(self, tree_index, l, r):
        '''
        递归创建线段树
        tree_index : 线段树节点在数组中位置
        l, r : 该节点表示的区间的左,右边界
        '''
        if l == r:
            self.tree[tree_index] = self.data[l]
            return
        mid = (l+r) // 2 # 区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = 2 * tree_index + 1, 2 * tree_index + 2 # tree_index的左右子树索引
        self._build(left, l, mid)
        self._build(right, mid+1, r)
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])

    def _query(self, tree_index, l, r, ql, qr):
        '''
        递归查询区间[ql,..,qr]的值
        tree_index : 某个根节点的索引
        l, r : 该节点表示的区间的左右边界
        ql, qr: 待查询区间的左右边界
        '''
        if l == ql and r == qr:
            return self.tree[tree_index]

        mid = (l+r) // 2 # 区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = tree_index * 2 + 1, tree_index * 2 + 2
        if qr <= mid:
            # 查询区间全在左子树
            return self._query(left, l, mid, ql, qr)
        elif ql > mid:
            # 查询区间全在右子树
            return self._query(right, mid+1, r, ql, qr)

        # 查询区间一部分在左子树一部分在右子树
        return self._merge(self._query(left, l, mid, ql, mid), 
                          self._query(right, mid+1, r, mid+1, qr))

    def _update(self, tree_index, l, r, index):
        '''
        tree_index:某个根节点索引
        l, r : 此根节点代表区间的左右边界
        index : 更新的值的索引
        '''
        if l == r == index:
            self.tree[tree_index] = self.data[index]
            return
        mid = (l+r)//2
        left, right = 2 * tree_index + 1, 2 * tree_index + 2
        if index > mid:
            # 要更新的区间在右子树
            self._update(right, mid+1, r, index)
        else:
            # 要更新的区间在左子树index<=mid
            self._update(left, l, mid, index)
        # 里面的小区间变化了，包裹的大区间也要更新
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        arr = []
        left, right, depth = dict(), dict(), dict()
        def dfs(cur,d):
            depth[cur.val] = d 
            if not cur.left and not cur.right:
                v = cur.val
                left[v] = len(arr)
                right[v] = len(arr)
                arr.append(d)
                return left[v], right[v]
            l, r = float('inf'), -float('inf')
            if cur.left:
                nl, nr = dfs(cur.left, d+1)
                l = min(l, nl)
                r = max(r, nr)
            if cur.right:
                nl, nr = dfs(cur.right, d+1)
                l = min(l, nl)
                r = max(r, nr)
            v = cur.val
            left[v] = l 
            right[v] = r 
            return l, r
        dfs(root, 0)

        # print(left,right)
        n = len(arr)
        seg = SegmentTree(arr)
        ans = []
        for q in queries:
            mx = depth[q]-1
            l, r = left[q], right[q]
            if l > 0:
                mx = max(mx, seg.query(0,l-1))
            if r < n-1:
                mx = max(mx, seg.query(r+1,n-1))
            ans.append(mx)
        return ans 