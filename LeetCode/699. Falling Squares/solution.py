# class Solution:
#     def fallingSquares(self, positions: List[List[int]]) -> List[int]:
#         res, ans = [], [0]
#         for l, w in positions:
#             r, h = l + w, w
#             for left, right, height in res:
#                 if right <= l or left >= r:
#                     continue
#                 h = max(h, height+w)
#             res.append((l,r,h))
#             ans.append(max(ans[-1],h))
#         return ans[1:]

# class SegTree:
#     def __init__(self, N):
#         self.tree = [0]*(4*N)
#         self.N = N

#     def query(self, left, right):
#         return self.query_(0,0,self.N-1,left,right)

#     def query_(self, idx, lo, hi, left, right):
#         if hi < left or lo > right:
#             return 0
#         if left <= lo and right >= hi:
#             return self.tree[idx]
#         mid = (lo+hi)//2
#         return max(self.query_(idx*2+1,lo,mid,left,right),self.query_(idx*2+2,mid+1,hi,left,right))

#     def update(self, left, right, val):
#         self.update_(0,0,self.N-1,left,right,val)

#     def update_(self, idx, lo, hi, left, right, val):
#         if hi < left or lo > right:
#             return
#         self.tree[idx] = max(self.tree[idx], val)
#         if lo < hi:
#             mid = (lo+hi)//2
#             self.update_(idx*2+1,lo,mid,left,right,val)
#             self.update_(idx*2+2,mid+1,hi,left,right,val)
#         return



# class Solution:
#     def fallingSquares(self, positions: List[List[int]]) -> List[int]:
#         positions_set = set()
#         for l, w in positions:
#             positions_set.add(l)
#             positions_set.add(l+w-1)
#         mp = {}
#         N = len(positions_set)
#         for i, p in enumerate(sorted(list(positions_set))):
#             mp[p] = i 
#         res = []
#         tree = SegTree(N)
#         for l, w in positions:
#             left, right = mp[l], mp[l+w-1]
#             h = tree.query(left, right)
#             tree.update(left, right, h+w)
#             res.append(tree.query(0,N-1))
#         return res


class SegTree:
    def __init__(self, N):
        self.tree = [0]*(4*N)
        self.lazy = [0]*(4*N)
        self.N = N

    def query(self, left, right):
        return self.query_(0,0,self.N-1,left,right)

    def query_(self, idx, lo, hi, left, right):
        if self.lazy[idx] > 0:
            self.tree[idx] = max(self.tree[idx], self.lazy[idx])
            if lo < hi:
                self.lazy[idx*2+1] = max(self.lazy[idx*2+1], self.lazy[idx])
                self.lazy[idx*2+2] = max(self.lazy[idx*2+2], self.lazy[idx])
            self.lazy[idx] = 0
        if hi < left or lo > right:
            return 0
        if left <= lo and right >= hi:
            return self.tree[idx]
        mid = (lo+hi)//2
        return max(self.query_(idx*2+1,lo,mid,left,right),self.query_(idx*2+2,mid+1,hi,left,right))

    def update(self, left, right, val):
        self.update_(0,0,self.N-1,left,right,val)

    def update_(self, idx, lo, hi, left, right, val):
        if self.lazy[idx] > 0:
            self.tree[idx] = max(self.tree[idx], self.lazy[idx])
            if lo < hi:
                self.lazy[idx*2+1] = max(self.lazy[idx*2+1], self.lazy[idx])
                self.lazy[idx*2+2] = max(self.lazy[idx*2+2], self.lazy[idx])
            self.lazy[idx] = 0
        if hi < left or lo > right:
            return
        
        if left <= lo and right >= hi:
            self.lazy[idx] = val
            return 
        self.tree[idx] = max(self.tree[idx], val)
        mid = (lo+hi)//2
        self.update_(idx*2+1,lo,mid,left,right,val)
        self.update_(idx*2+2,mid+1,hi,left,right,val)
        return



class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        positions_set = set()
        for l, w in positions:
            positions_set.add(l)
            positions_set.add(l+w-1)
        mp = {}
        N = len(positions_set)
        for i, p in enumerate(sorted(list(positions_set))):
            mp[p] = i 
        res = []
        tree = SegTree(N)
        for l, w in positions:
            left, right = mp[l], mp[l+w-1]
            h = tree.query(left, right)
            tree.update(left, right, h+w)
            res.append(tree.query(0,N-1))
        return res

