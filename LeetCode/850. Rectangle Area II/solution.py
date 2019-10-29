
# class Solution:
#     def rectangleArea(self, rectangles: List[List[int]]) -> int:
#         points = []
#         for rectangle in rectangles:
#             points.append((rectangle[0],rectangle[1],rectangle[3],rectangle[2]))
#             points.append((rectangle[2],-1,-1,-1))
#         points = sorted(points)
#         # print(points)
#         states = []
#         pre_x = points[0][0]
#         sums = 0
#         for point in points:
#             x, y1, y2, life = point
#             y, pre_y = 0, -1
#             for i, state in enumerate(states):
#                 if states[i][1] > pre_y:
#                     if states[i][0] < pre_y:
#                         y += states[i][1] - pre_y
#                     else:
#                         y += states[i][1] - states[i][0]
#                     pre_y = states[i][1]
            
#             sums += y*(x-pre_x)
#             pre_x = x

#             states = [state for state in states if state[-1] > x]
#             if y1 >= 0:
#                 states.append((y1,y2,life))
#                 states = sorted(states)
            
#         return sums%(10**9+7)

# class Solution(object):
#     def rectangleArea(self, rectangles):
#         # Populate events
#         OPEN, CLOSE = 0, 1
#         events = []
#         for x1, y1, x2, y2 in rectangles:
#             events.append((y1, OPEN, x1, x2))
#             events.append((y2, CLOSE, x1, x2))
#         events.sort()

#         def query():
#             ans = 0
#             cur = -1
#             for x1, x2 in active:
#                 cur = max(cur, x1)
#                 ans += max(0, x2 - cur)
#                 cur = max(cur, x2)
#             return ans

#         active = []
#         cur_y = events[0][0]
#         ans = 0
#         for y, typ, x1, x2 in events:
#             # For all vertical ground covered, update answer
#             ans += query() * (y - cur_y)

#             # Update active intervals
#             if typ is OPEN:
#                 active.append((x1, x2))
#                 active.sort()
#             else:    
#                 active.remove((x1, x2))

#             cur_y = y

#         return ans % (10**9 + 7)

# class Lines:
#     def __init__(self, x, y1, y2, In):
#         self.x = x
#         self.y1 = y1
#         self.y2 = y2
#         self.In = In
# class Node:
#     def __init__(self):
#         self.l = 0
#         self.r = 0
#         self.rval = 0
#         self.lval = 0
#         self.cover = 0
#         self.cnt = 0
# class Solution(object):
#     def rectangleArea(self, rectangles):
#         """
#         :type rectangles: List[List[int]]
#         :rtype: int
#         """
#         global L, Rank, Tree
#         L= []
#         Rank = []
#         mod = 1000000007
#         for i in range(len(rectangles)):
#             Rank.append(rectangles[i][1])
#             Rank.append(rectangles[i][3])
#             L.append(Lines(rectangles[i][0], rectangles[i][1], rectangles[i][3], 1))
#             L.append(Lines(rectangles[i][2], rectangles[i][1], rectangles[i][3], -1))
#         Rank = list(set(Rank))
#         Rank.sort()
#         L.sort(key=lambda A: A.x)
#         # print Rank
#         maxn = len(Rank)
#         Tree = [Node() for i in range(maxn << 2)]
#         self.build(0, maxn-1, 0)
#         self.update(0, L[0])
#         ans = 0
#         for i in range(1, len(L)):
#             ans += Tree[0].cnt * (L[i].x - L[i-1].x) % mod
#             self.update(0, L[i])
#         return ans%mod
#     def build(self, l, r, rt):
#         Tree[rt].l = l
#         Tree[rt].r = r
#         Tree[rt].lval = Rank[l]
#         Tree[rt].rval = Rank[r]
#         if r - l == 1:
#             return
#         m = (l + r)//2
#         self.build(l, m, 2*rt+1)
#         self.build(m, r, 2*rt+2)
#     def canlen(self, rt, line):
#         if Tree[rt].cover > 0:
#             Tree[rt].cnt = Tree[rt].rval - Tree[rt].lval
#             return
#         if Tree[rt].r - Tree[rt].l == 1:
#             Tree[rt].cnt = 0
#         else:
#             Tree[rt].cnt = Tree[2*rt+1].cnt + Tree[2*rt+2].cnt

#     def update(self, rt, line):
#         if Tree[rt].lval >= line.y1 and Tree[rt].rval <= line.y2:
#             Tree[rt].cover += line.In
#             self.canlen(rt, line)
#             return
#         if Tree[rt].rval <= line.y1 or Tree[rt].lval >= line.y2:
#             return
#         self.update(2*rt+1, line)
#         self.update(2*rt+2, line)
#         self.canlen(rt, line)


# 作者：vampire-3
# 链接：https://leetcode-cn.com/problems/rectangle-area-ii/solution/pythonchi-san-hua-sao-miao-xian-xian-duan-shu-by-v/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Node(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.total = self.count = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end)
        return self._right

    def update(self, i, j, val):
        if i >= j: return 0
        if self.start == i and self.end == j:
            self.count += val
        else:
            self.left.update(i, min(self.mid, j), val)
            self.right.update(max(self.mid, i), j, val)

        if self.count > 0:
            self.total = X[self.end] - X[self.start]
        else:
            self.total = self.left.total + self.right.total

        return self.total

class Solution(object):
    def rectangleArea(self, rectangles):
        OPEN, CLOSE = 1, -1
        events = []
        global X
        X = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
            X.add(x1)
            X.add(x2)
        events.sort()

        X = sorted(X)
        Xi = {x: i for i, x in enumerate(X)}

        active = Node(0, len(X) - 1)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]

        for y, typ, x1, x2 in events:
            ans += cur_x_sum * (y - cur_y)
            cur_x_sum = active.update(Xi[x1], Xi[x2], typ)
            cur_y = y

        return ans % (10**9 + 7)