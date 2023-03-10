class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0]*(4*self.n)
        self.lazy = [0]*(4*self.n)
        self._dfs(0,0,self.n-1)

    def _dfs(self, idx, l, r):
        if l == r:
            self.tree[idx] = self.arr[l]
            return  
        m = (l+r)//2
        self._dfs(idx*2+1, l, m)
        self._dfs(idx*2+2, m+1, r)
        self.tree[idx] = self.tree[idx*2+1] + self.tree[idx*2+2]
        return

    def _push(self, idx):
        self.lazy[idx*2+1] ^= 1 
        self.lazy[idx*2+2] ^= 1
        return

    def update(self, idx, l, r, lo, hi):
        if self.lazy[idx]:
            self.lazy[idx] = 0
            self.tree[idx] = r-l+1-self.tree[idx]
            if l < r:
                self._push(idx)

        if r < lo or l > hi:
            return
        if lo <= l and r <= hi:
            self.tree[idx] = r-l+1-self.tree[idx]
            if l < r:
                self._push(idx)
            return
        m = (l+r)//2
        self.update(idx*2+1,l,m,lo,hi)
        self.update(idx*2+2,m+1,r,lo,hi)
        self.tree[idx] = self.tree[idx*2+1] + self.tree[idx*2+2]
        return




class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        s = sum(nums2)
        cnt = sum(nums1)
        T = SegTree(nums1)
        n = len(nums1)
        for op, lo, hi in queries:
            if op == 1:
                T.update(0,0,n-1,lo,hi)
                cnt = T.tree[0]
            elif op == 2:
                s += lo*cnt
            else:
                ans.append(s)
        return ans 
