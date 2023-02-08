class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def calc(x,y):
            return sum(((x-xx)**2+(y-yy)**2)**0.5 for xx, yy in positions)
        x, y, r = 0, 0, 100
        epsilon = 10**-8
        dxy = [[-1,0],[0,-1],[1,0],[0,1]]
        while r > epsilon:
            flag = False
            cur = calc(x,y)
            for dx, dy in dxy:
                dx *= r 
                dy *= r 
                dx += x 
                dy += y 
                nxt = calc(dx,dy)
                if nxt < cur:
                    flag = True
                    x, y = dx, dy 
                    break
            if not flag:
                r /= 2 
        # print(x,y,r)
        return calc(x,y)



class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:

        def func(x,y):
            return sum(((x-px)**2+(y-py)**2)**0.5 for px,py in positions)


        step, alpha, epsilon = 100, 0.99, 0.0000001
        x, y = 0, 0
        while True:
            prex, prey = x, y 
            # 注意分母为零
            dx = sum((x-px)/(((x-px)**2+(y-py)**2)**(0.5)+epsilon) for px,py in positions)
            dy = sum((y-py)/(((x-px)**2+(y-py)**2)**(0.5)+epsilon) for px,py in positions)
            # print(x,y,dx,dy)
            x -= dx*step
            y -= dy*step
            if ((x-prex)**2+(y-prey)**2)**0.5 < epsilon:
                break           
            step *= alpha
        # print(x,y)
        return func(x,y)



class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        epsilon, delta = 1e-6, 0.001
        def func(x,y):
            return sum(((x-px)**2+(y-py)**2)**0.5 for px,py in positions)

        def check(x):
            yl, yr = 0, 100
            while yr-yl > epsilon:
                y1 = yl*(0.5+delta) + yr*(0.5-delta)
                y2 = yl*(0.5-delta) + yr*(0.5+delta)
                f1, f2 = func(x,y1), func(x,y2)
                if f1 < f2:
                    yr = y2
                else:
                    yl = y1
            return (f1+f2)/2

        xl, xr = 0, 100
        while xr-xl > epsilon:
            x1 = xl*(0.5+delta) + xr*(0.5-delta)
            x2 = xl*(0.5-delta) + xr*(0.5+delta)
            c1, c2 = check(x1), check(x2)
            if c1 < c2:
                xr = x2
            else:
                xl = x1
        return (c1+c2)/2


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # 到各点距离之和
        def dis(x, y):
            return sum([((px - x) ** 2 + (py - y) ** 2) ** 0.5 for px, py in positions])

        # 三分找最小
        def three_divide(l, r, f, eps=1e-6):
            while r - l > eps:
                m = l + (r - l) / 3
                mm = r - (r - l) / 3
                if f(m) < f(mm):
                    r = mm
                else:
                    l = m
            return f((l + r) / 2)

        # 左右边界
        lmin, rmax = 0, 100

        # 外层查x,x=mx时最小距离
        def xf(mx):
            # 内层查y,x=mx且y=my的距离
            def yf(my): return dis(mx, my)
            return three_divide(lmin, rmax, yf)

        return three_divide(lmin, rmax, xf)


作者：lyhshang
链接：https://leetcode-cn.com/problems/best-position-for-a-service-centre/solution/san-fen-tao-san-fen-by-lyhshang/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:    
    def getMinDistSum(self, P: List[List[int]]) -> float:
        from math import sqrt
        def dist_all(x, y):  # calculate the sum of distances from (x, y) to all points
            return sum(sqrt((x2-x)**2 + (y2-y)**2) for x2, y2 in P)

        l = len(P)
        x, y = sum(x for x, y in P) / l, sum(y for x, y in P) / l  # use centroid as the start point
        d = dist_all(x, y)  # sum of distances for initial point
        
        # step: inital searching step. choosing 10 since all point coordinates are in range [0, 100]
        # eps: since the problem demands an accuracy of 10^-5. I choose a smaller one, no reason
        # these two numbers are kind of arbitrarily choosen
        step, eps = 100, 1e-6
        while step > eps:
            flag = False  # Do we find a better point in this round?
            for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                x2, y2 = x + step * dx, y + step * dy
                t = dist_all(x2, y2)
                if t < d:  # do find a better solution point
                    x, y, d = x2, y2, t
                    flag = True
                    break
            if not flag: step *= 0.5  # if no better point is found, shrink ths step for a closer search
        return d


# class Solution:
#     def getMinDistSum(self, positions: List[List[int]]) -> float:
#         def func(x,y):
#             return sum(((x-px)**2+(y-py)**2)**0.5 for px,py in positions)

#         def gx(x,y):
#             return (func(x+delta,y)-func(x,y))/delta

#         def gy(x,y):
#             return (func(x,y+delta)-func(x,y))/delta

#         delta = epsilon  = 0.00000001
#         step = 1
#         n = len(positions)
#         x, y = sum(px for px,py in positions)/n, sum(py for px,py in positions)/n
#         # x, y = sum(px for px,py in positions)/n, 0
#         f = func(x,y)
#         # flag = 1
#         while True:
#             dx = -gx(x,y)
#             dy = -gy(x,y)
#             # dx = -sum((x-px) for px,py in positions)
#             # dy = -sum((y-py) for px,py in positions)
#             # print(x,y,dx,dy)
#             # x += dx*step
#             # y += dy*step
#             if dx > 0:
#                 dx = 1
#             elif dx < 0:
#                 dx = -1
#             if dy > 0:
#                 dy = 1
#             elif dy < 0:
#                 dy = -1
#             # x += dx*step*flag
#             # y += dy*step*(1-flag)
#             x += dx*step
#             y += dy*step
#             tmp = func(x,y)
#             # if abs(tmp - f) < epsilon:
#             #     break
#             f = tmp
#             # if step < epsilon:
#             #     break
#             if abs(dx*step) < epsilon and abs(dy*step) < epsilon:
#                 break
#             step *= 0.99
#             # flag = 1-flag
#         # print(x,y)
#         return f




# class Solution:
#     def getMinDistSum(self, positions: List[List[int]]) -> float:
#         def func(x,y):
#             return sum(((x-px)**2+(y-py)**2)**0.5 for px,py in positions)

#         def gx(x,y):
#             return (func(x+delta,y)-func(x,y))/delta

#         def gy(x,y):
#             return (func(x,y+delta)-func(x,y))/delta

#         delta, epsilon  = 0.0000001, 0.00001
#         step = 1
#         n = len(positions)
#         x, y = sum(px for px,py in positions)/n, sum(py for px,py in positions)/n
#         # x, y = sum(px for px,py in positions)/n, 0
#         f = func(x,y)
#         # flag = 1
#         while True:
#             dx = -gx(x,y)
#             dy = -gy(x,y)
#             # print(dx,dy)
#             # dx = -sum((x-px) for px,py in positions)
#             # dy = -sum((y-py) for px,py in positions)
#             # print(x,y,dx,dy)
#             # x += dx*step
#             # y += dy*step
#             if dx > 0:
#                 dx = 1
#             elif dx < 0:
#                 dx = -1
#             if dy > 0:
#                 dy = 1
#             elif dy < 0:
#                 dy = -1
#             # x += dx*step*flag
#             # y += dy*step*(1-flag)
#             # x += dx*step
#             # y += dy*step
#             # tmp = func(x,y)
#             tmp = func(x+dx*step,y+dy*step)
#             # print(x,y,step,f,tmp)
#             if tmp < f:
#                 x += dx*step
#                 y += dy*step
#                 f = tmp
#                 # print(x,y)
#             else:
#                 step *= 0.5
#             # x += dx*step
#             # y += dy*step
#             # if abs(tmp - f) < epsilon:
#             #     break
            
#             # f = tmp
#             # if step < epsilon:
#             #     break
#             if abs(dx*step) < epsilon and abs(dy*step) < epsilon:
#                 break
#             # step *= 0.9
#             # flag = 1-flag
#         # print(x,y)
#         return f
