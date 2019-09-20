class NumArray:

    def __init__(self, nums: List[int]):
        if not nums: return
        n = len(nums)
        tree = [0]*(4*n)
        def build(lo, hi, idx):
            if lo == hi:
                tree[idx] = nums[lo]
                return tree[idx]
            mid = (lo + hi)//2
            tree[idx] = build(lo, mid, idx*2 + 1) + build(mid + 1, hi, idx*2 + 2)
            return tree[idx]
        build(0, n-1, 0)
        self.nums = nums
        self.tree = tree
        self.n = n
        return

    def update(self, i: int, val: int) -> None:
        delta = val - self.nums[i]
        self.nums[i] = val
        def update_(pos, lo, hi, idx):
            mid = (lo+hi)//2
            if lo == hi:
                self.tree[idx] += delta
                return
            if pos <= mid:
                update_(pos, lo, mid, idx*2+1)
            else:
                update_(pos, mid+1, hi, idx*2+2)
            self.tree[idx] = self.tree[idx*2+1] + self.tree[idx*2+2]
            return
        
        update_(i, 0, self.n-1, 0)
        return
        
        
    def sumRange(self, i: int, j: int) -> int:
        
        def query(left, right, lo, hi, idx):
            if lo > right or hi < left:
                return 0
            if lo >= left and hi <= right:
                return self.tree[idx]
            mid = (lo + hi)//2
            return query(left,right,lo,mid,idx*2+1) + query(left,right,mid+1,hi,idx*2+2)
        return query(i,j,0,self.n-1,0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)