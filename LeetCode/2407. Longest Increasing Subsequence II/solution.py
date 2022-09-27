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


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        arr = sorted(set(nums))
        mp = {v: i for i, v in enumerate(arr)}
        n = len(nums)
        seg = SegmentTree([0]*n)
        ans = 0
        for v in nums:
            left = bisect.bisect_left(arr,v-k)
            right = mp[v]-1
            pre = 0
            if right >= left:
                pre = seg.query(left,right)
            ans = max(ans,pre+1)
            tmp = seg.query(right+1,right+1)
            # print(v,left,right,pre,tmp)
            if pre+1 > tmp:
                seg.update(right+1,pre+1)
            # print(seg.query(right+1,right+1),seg.arr)
        return ans


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        u = max(nums)
        mx = [0] * (4 * u)

        def modify(o: int, l: int, r: int, i: int, val: int) -> None:
            if l == r:
                mx[o] = val
                return
            m = (l + r) // 2
            if i <= m: modify(o * 2, l, m, i, val)
            else: modify(o * 2 + 1, m + 1, r, i, val)
            mx[o] = max(mx[o * 2], mx[o * 2 + 1])

        # 返回区间 [L,R] 内的最大值
        def query(o: int, l: int, r: int, L: int, R: int) -> int:  # L 和 R 在整个递归过程中均不变，将其大写，视作常量
            if L <= l and r <= R: return mx[o]
            res = 0
            m = (l + r) // 2
            if L <= m: res = query(o * 2, l, m, L, R)
            if R > m: res = max(res, query(o * 2 + 1, m + 1, r, L, R))
            return res

        for x in nums:
            if x == 1:
                modify(1, 1, u, 1, 1)
            else:
                res = 1 + query(1, 1, u, max(x - k, 1), x - 1)
                modify(1, 1, u, x, res)
        return mx[1]


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/longest-increasing-subsequence-ii/solution/zhi-yu-xian-duan-shu-pythonjavacgo-by-en-p1gz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class SegTree:
    def __init__(self, N):
        self.arr = [0]*(N*4)
        self.N = N

    def update(self, pos, val):
        self.update_(0, 1, self.N, pos, val)
        return

    def update_(self, idx, lo, hi, pos, val):
        if lo > pos or hi < pos:
            return
        if lo == hi:
            self.arr[idx] = val
            return
        mid = (lo + hi)//2
        self.update_(idx*2+1, lo, mid, pos, val)
        self.update_(idx*2+2, mid+1, hi, pos, val)
        self.arr[idx] = max(self.arr[idx*2+1], self.arr[idx*2+2])    
        return

    def query(self, left, right):
        return self.query_(0, 1, self.N, left, right)

    def query_(self, idx, lo, hi, left, right):
        if lo > right or hi < left:
            return 0
        if lo >= left and hi <= right:
            return self.arr[idx]
        mid = (lo + hi)//2
        return max(self.query_(idx*2+1,lo,mid,left,right), self.query_(idx*2+2,mid+1,hi,left,right))


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        arr = sorted(set(nums))
        mp = {v: i+1 for i, v in enumerate(arr)}
        n = len(nums)
        seg = SegTree(n)
        ans = 0
        for v in nums:
            left = bisect.bisect_left(arr,v-k)+1
            right = mp[v]-1
            pre = 0
            if right >= left:
                pre = seg.query(left,right)
            ans = max(ans,pre+1)
            tmp = seg.query(right+1,right+1)
            # print(v,left,right,pre,tmp)
            if pre+1 > tmp:
                seg.update(right+1,pre+1)
            # print(seg.query(right+1,right+1),seg.arr)
        return ans 