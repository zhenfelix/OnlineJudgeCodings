# from bisect import bisect_left as bl, bisect_right as br

# class RangeModule:

#     def __init__(self):
#         self.intervals = []

#     def addRange(self, left: int, right: int) -> None:
#         lo, hi = [], []
#         for a, b in self.intervals:
#             if b < left:
#                 lo.append((a,b))
#             elif a > right:
#                 hi.append((a,b))
#             else:
#                 left = min(left, a)
#                 right = max(right, b)
#         self.intervals = lo + [(left,right)] + hi
#         return


#     def queryRange(self, left: int, right: int) -> bool:
#         # print(self.intervals,left,right)
#         i = bl(self.intervals, (left,float('inf')))
#         return i > 0 and self.intervals[i-1][-1] >= right

#     def removeRange(self, left: int, right: int) -> None:
#         lo, hi = [], []
#         for a, b in self.intervals:
#             if b <= left:
#                 lo.append((a,b))
#             elif a >= right:
#                 hi.append((a,b))
#             else:
#                 if a < left:
#                     lo.append((a,left))
#                 if b > right:
#                     hi.append((right,b))
#         self.intervals = lo + hi 
#         return 


class RangeModule:

    def __init__(self):
        self.root = SegNode(0,10**9,False)

    def update(self, cur, left, right, state):
        
        if cur.l >= left and cur.r <= right:
            cur.state = state
            cur.left, cur.right = None, None
            return state
        if cur.l >= right or cur.r <= left:
            return cur.state
        if not cur.left:
            mid = (cur.l+cur.r)//2
            cur.left = SegNode(cur.l,mid,cur.state)
            cur.right = SegNode(mid,cur.r,cur.state)
        sl = self.update(cur.left,left,right,state)
        sr = self.update(cur.right,left,right,state)
        cur.state = (sl and sr)
        return cur.state

    def query(self, cur, left, right):
        # print(cur,left,right)
        if cur.l >= right or cur.r <= left:
            return True
        if (cur.l >= left and cur.r <= right) or not cur.left:
            return cur.state
        
        res = self.query(cur.left,left,right) and self.query(cur.right,left,right)
        # print(cur,left,right,res)
        return res



    def addRange(self, left, right):
        self.update(self.root,left,right,True)
        

    def queryRange(self, left, right):
        return self.query(self.root,left,right)
        

    def removeRange(self, left, right):
        self.update(self.root,left,right,False)


class SegNode:

    def __init__(self,l,r,state):
        self.l, self.r, self.state = l, r, state
        self.left, self.right = None, None
        
    def __repr__(self):
        return ' '.join(map(str,[self.l,self.r,self.state]))


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)