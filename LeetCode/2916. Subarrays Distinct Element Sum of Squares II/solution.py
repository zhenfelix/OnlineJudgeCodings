class SegmentTree:
    def __init__(self, n):
        self.n = n 
        self.B1 = [0]*n 
        self.B2 = [0]*n  


    def add(self, b, idx, x):
        N = self.n 
        while idx < N:
            b[idx] += x
            idx += idx & -idx

    def range_add(self, l,r,x):
        B1 = self.B1
        B2 = self.B2
        self.add(B1, l, x)
        self.add(B1, r+1, -x)
        self.add(B2, l, x*(l-1))
        self.add(B2, r+1, -x*r)

    def sum(self, b, idx):
        total = 0
        while idx > 0:
            total += b[idx]
            idx -= idx & -idx
        return total

    def prefix_sum(self, idx):
        B1 = self.B1
        B2 = self.B2
        return self.sum(B1, idx)*idx -  self.sum(B2, idx)

    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l-1)

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        seg = SegmentTree(n+5)
        MOD = 10**9+7
        seen = dict()
        ans, cur = 0, 0 
        for i, a in enumerate(nums):
            j = -1 if a not in seen else seen[a]
            s = seg.range_sum(j+2,i+1)
            cur += s*2+i-j
            cur %= MOD 
            ans += cur
            ans %= MOD
            # print(i,s,cur)
            seg.range_add(j+2,i+1,1)
            seen[a] = i
        return ans 

class Node(object): #线段树
    def __init__(self, lid = 0, rid = 0):
        self.val = 0
        self.lazy = 0
        self.lid = lid
        self.rid = rid
        self.left = None
        self.right = None

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        self.base = 10 ** 9 + 7
        n = len(nums)
        left = {}
        root = self.build(0, n - 1)
        s2 = [0] * n
        for i, num in enumerate(nums):
            l = left.get(num, -1)
            s2[i] = (s2[i - 1] + self.query(root, l + 1, i) * 2 + i - l) % self.base
            self.update(root, l + 1, i, 1)
            left[num] = i
        return sum(s2) % self.base

    def build(self, l, r): #建立线段树
        if l == r:
            return Node(l, r)
        root = Node(l, r)
        m = (l + r) >> 1
        root.left = self.build(l, m)
        root.right = self.build(m + 1, r)
        return root

    def update(self, root, l1, r1, add):
        l = root.lid
        r = root.rid
        if r < l1 or l > r1: #当前区间和待更新区间无交集, 不处理
            pass
        elif l1 <= l and r <= r1: #当前区间包含于待更新区间, 懒操作
            root.val = (root.val + add * (r - l + 1)) % self.base #val包含lazy部分
            root.lazy = (root.lazy + add) % self.base
        else:
            if root.lazy != 0:
                self.update(root.left, root.left.lid, root.left.rid, root.lazy)
                self.update(root.right, root.right.lid, root.right.rid, root.lazy)
                root.lazy = 0
            root.val = (self.update(root.left, l1, r1, add) + self.update(root.right, l1, r1, add)) % self.base
        return root.val

    def query(self, root, l1, r1):
        l = root.lid
        r = root.rid
        if r < l1 or l > r1: #当前区间和查询区间无交集
            return 0
        if l1 <= l and r <= r1: #当前区间包含于查询区间, 返回整个区间结果
            return root.val
        if root.lazy != 0: #lazy下放
            self.update(root.left, root.left.lid, root.left.rid, root.lazy)
            self.update(root.right, root.right.lid, root.right.rid, root.lazy)
            root.lazy = 0
        return (self.query(root.left, l1, r1) + self.query(root.right, l1, r1)) % self.base