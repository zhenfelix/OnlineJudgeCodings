# class Solution:
#     def pileBox(self, box: List[List[int]]) -> int:
#         box.sort()
#         n = len(box)
#         dp = [0]*n 
#         for i in range(n):
#             h = 0
#             for j in range(i):
#                 if all(box[j][k] < box[i][k] for k in range(3)):
#                     h = max(h, dp[j])
#             dp[i] = h+box[i][2]
#         return max(dp)

class BIT:
    def __init__(self,n,m):
        self.tree = [[0]*(m+1) for _ in range(n+1)]
        self.n, self.m = n, m 

    def query(self,qx,qy):
        res = 0
        x = qx
        while x:
            y = qy
            while y:
                res = max(res, self.tree[x][y])
                y -= y&(-y)
            x -= x&(-x)
        return res

    def update(self,qx,qy,val):
        n, m = self.n, self.m
        x = qx
        while x <= n:
            y = qy
            while y <= m:
                self.tree[x][y] = max(self.tree[x][y], val)
                y += y&(-y)
            x += x&(-x)


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        box.sort(key=lambda x: (x[-1],-x[0],-x[1]))
        w2id, d2id = {}, {}
        ws = sorted(list(set([w for w,_,_ in box])))
        for i, w in enumerate(ws,1):
            w2id[w] = i
        ds = sorted(list(set([d for _,d,_ in box])))
        for i, d in enumerate(ds,1):
            d2id[d] = i
        n, m = len(ws), len(ds)
        T = BIT(n,m)
        res = 0
        for w,d,h in box:
            hsum = T.query(w2id[w]-1,d2id[d]-1)
            T.update(w2id[w],d2id[d],hsum+h)
            res = max(res,hsum+h)
        return res






class SegmentTree:
    def __init__(self,n,m):
        self.tree = [[0]*(4*(m+1)) for _ in range(4*(n+1))]
        self.n, self.m = n, m 

    def query(self,qxl,qxr,qyl,qyr):
        def query_y(xl,xr,vx,yl,yr,vy):
            if yr < qyl or yl > qyr:
                return 0
            if yl >= qyl and yr <= qyr:
                return self.tree[vx][vy]
            else:
                ym = (yl+yr)//2
                return max(query_y(xl,xr,vx,yl,ym,vy*2+1),query_y(xl,xr,vx,ym+1,yr,vy*2+2))

        def query_x(xl,xr,vx):
            if xr < qxl or xl > qxr:
                return 0
            if xl >= qxl and xr <= qxr:
                return query_y(xl,xr,vx,0,self.m,0)
            else:
                xm = (xl+xr)//2
                return max(query_x(xl,xm,vx*2+1),query_x(xm+1,xr,vx*2+2))

        return query_x(0,self.n,0)

    def update(self,x,y,val):
        def update_y(xl,xr,vx,yl,yr,vy):
            if yl == yr:
                if xl == xr:
                    self.tree[vx][vy] = val
                else:
                    self.tree[vx][vy] = max(self.tree[vx*2+1][vy],self.tree[vx*2+2][vy])
            else:
                ym = (yl+yr)//2
                if y <= ym:
                    update_y(xl,xr,vx,yl,ym,vy*2+1)
                else:
                    update_y(xl,xr,vx,ym+1,yr,vy*2+2)
                self.tree[vx][vy] = max(self.tree[vx][vy*2+1],self.tree[vx][vy*2+2])
            return



        def update_x(xl,xr,vx):
            if xl < xr:
                xm = (xl+xr)//2
                if x <= xm:
                    update_x(xl,xm,vx*2+1)
                else:
                    update_x(xm+1,xr,vx*2+2)
            update_y(xl,xr,vx,0,self.m,0)
            return

        update_x(0,self.n,0)


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        box.sort(key=lambda x: (x[-1],-x[0],-x[1]))
        w2id, d2id = {}, {}
        ws = sorted(list(set([w for w,_,_ in box])))
        for i, w in enumerate(ws,1):
            w2id[w] = i
        ds = sorted(list(set([d for _,d,_ in box])))
        for i, d in enumerate(ds,1):
            d2id[d] = i
        n, m = len(ws), len(ds)
        T = SegmentTree(n,m)
        res = 0
        for w,d,h in box:
            hsum = T.query(0,w2id[w]-1,0,d2id[d]-1)
            T.update(w2id[w],d2id[d],hsum+h)
            res = max(res,hsum+h)
        return res

