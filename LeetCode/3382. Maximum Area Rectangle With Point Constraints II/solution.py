class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        ys = sorted(set(yCoord))
        mp = {y:i+1 for i, y in enumerate(ys)}
        m = len(ys)+5
        arr = [0]*m
        def update(i):
            while i < m:
                arr[i] += 1
                i += i&-i
            return
        def query(i):
            res = 0
            while i > 0:
                res += arr[i]
                i -= i&-i
            return res
        n = len(xCoord)
        xy = []
        for i in range(n):
            xy.append((xCoord[i],yCoord[i]))
        xy.sort()
        pre = dict()
        n = len(xy)
        ans = -1
        for i, (x,y) in enumerate(xy):
            update(mp[y])
            if i > 0 and (xy[i-1][0] == x):
                cnt = query(mp[y])-query(mp[xy[i-1][1]]-1)
                if y in pre:
                    j, cnt_old = pre[y]
                    if j > 0 and (xy[j-1][1] == xy[i-1][1]) and (cnt-cnt_old == 2):
                        x1, y1 = xy[j-1]
                        ans = max(ans,abs((x-x1)*(y-y1)))
                pre[y] = (i,cnt)
        return ans 



