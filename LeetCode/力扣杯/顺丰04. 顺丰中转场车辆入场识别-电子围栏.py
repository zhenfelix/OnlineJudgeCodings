class Solution:
    def isPointInPolygon(self, x: float, y: float, coords: List[float]) -> bool:
        xx, yy = [], []
        for a, b in zip(coords[::2], coords[1::2]):
            xx.append(a)
            yy.append(b)
        n = len(xx)
        cnt = 0
        def detect(x1,y1,x2,y2):
            if y > max(y1,y2) or y < min(y1,y2) or x > max(x1,x2):
                return False
            if x < min(x1,x2):
                return True
            if x1 < x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            return ((x1-x)*(y1-y2)-(x1-x2)*(y1-y))*(y1-y2) > 0
            
        for i in range(1,n):
            x1, y1 = xx[i], yy[i]
            x2, y2 = xx[i-1], yy[i-1]
            if y == y1 and x < x1:
                cnt += 1
            if y not in [y1,y2] and detect(x1,y1,x2,y2):
                # print(x1,y1,x2,y2)
                cnt += 1
        # print(cnt)
        if cnt == 1:
            return True
        return False